import json
from pathlib import Path
from typing import Dict, List


MANIFEST_PATH = Path("data/demo_asset_manifest.json")


TYPE_TO_FOLDER = {
    "character": "characters",
    "enemy": "enemies",
    "item": "items",
    "tile": "tiles",
    "ui": "ui",
    "background": "backgrounds",
    "other": "items"
}


def load_demo_manifest() -> List[dict]:
    """Load demo asset manifest."""
    if not MANIFEST_PATH.exists():
        return []

    with MANIFEST_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def normalize_text(text: str) -> str:
    """Normalize text for simple keyword matching."""
    if not text:
        return ""
    return str(text).strip().lower()


def match_demo_asset(asset: dict, manifest: List[dict], fallback_counter: Dict[str, int]) -> dict:
    """Match one requested asset to demo asset pool."""
    asset_type = normalize_text(asset.get("asset_type", "other"))
    display_name = normalize_text(asset.get("display_name", ""))
    description = normalize_text(asset.get("description_zh", ""))

    query = f"{display_name} {description}"

    same_type_assets = [
        item for item in manifest
        if normalize_text(item.get("asset_type")) == asset_type
    ]

    # 1. exact keyword match
    for item in same_type_assets:
        keywords = item.get("keywords", [])
        for keyword in keywords:
            if normalize_text(keyword) and normalize_text(keyword) in query:
                return {
                    "matched_asset_key": item.get("asset_key"),
                    "image_path": item.get("file_path"),
                    "match_strategy": "精准匹配",
                    "demo_display_name": item.get("display_name")
                }

    # 2. same type fallback rotation
    if same_type_assets:
        index = fallback_counter.get(asset_type, 0) % len(same_type_assets)
        fallback_counter[asset_type] = fallback_counter.get(asset_type, 0) + 1
        item = same_type_assets[index]
        return {
            "matched_asset_key": item.get("asset_key"),
            "image_path": item.get("file_path"),
            "match_strategy": "同类型替代",
            "demo_display_name": item.get("display_name")
        }

    # 3. global fallback
    if manifest:
        item = manifest[0]
        return {
            "matched_asset_key": item.get("asset_key"),
            "image_path": item.get("file_path"),
            "match_strategy": "全局替代",
            "demo_display_name": item.get("display_name")
        }

    return {
        "matched_asset_key": None,
        "image_path": "",
        "match_strategy": "未匹配",
        "demo_display_name": ""
    }


def generate_demo_assets(asset_list: List[dict], prompts: List[dict]) -> List[dict]:
    """Generate demo asset records by matching requested assets to built-in demo pool."""
    manifest = load_demo_manifest()
    fallback_counter = {}

    prompt_map = {
        item.get("asset_id"): item
        for item in prompts
    }

    results = []

    for asset in asset_list:
        if not asset.get("selected", True):
            continue

        matched = match_demo_asset(asset, manifest, fallback_counter)
        prompt_record = prompt_map.get(asset.get("asset_id"), {})

        results.append(
            {
                "asset_id": asset.get("asset_id"),
                "asset_type": asset.get("asset_type", "other"),
                "display_name": asset.get("display_name", "未命名素材"),
                "description_zh": asset.get("description_zh", ""),
                "image_path": matched.get("image_path", ""),
                "match_strategy": matched.get("match_strategy", ""),
                "demo_display_name": matched.get("demo_display_name", ""),
                "generation_mode": "Demo Mode",
                "prompt": prompt_record.get("prompt", ""),
                "negative_prompt": prompt_record.get("negative_prompt", "")
            }
        )

    return results
