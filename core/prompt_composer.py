import json
from pathlib import Path
from typing import Dict, List


PROMPT_TEMPLATE_PATH = Path("data/prompt_templates.json")


def load_prompt_templates() -> Dict[str, dict]:
    """Load prompt templates from JSON."""
    if not PROMPT_TEMPLATE_PATH.exists():
        return {}

    with PROMPT_TEMPLATE_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def normalize_asset_type(asset_type: str) -> str:
    """Normalize asset type for template lookup."""
    if not asset_type:
        return "other"

    asset_type = asset_type.strip().lower()
    allowed_types = {"character", "enemy", "item", "tile", "ui", "background"}
    return asset_type if asset_type in allowed_types else "other"


def compose_prompt(asset: dict, style_profile: dict) -> dict:
    """Compose a game-aware prompt for a single asset."""
    templates = load_prompt_templates()

    asset_type = normalize_asset_type(asset.get("asset_type", "other"))
    template = templates.get(asset_type, templates.get("other", {}))

    prompt_pattern = template.get(
        "prompt_pattern",
        "2D game asset of {display_name}, {description_zh}, {style_prompt}, {size}, game-ready asset"
    )

    prompt = prompt_pattern.format(
        display_name=asset.get("display_name", "unnamed asset"),
        description_zh=asset.get("description_zh", ""),
        style_prompt=style_profile.get("style_prompt", ""),
        view=style_profile.get("view", ""),
        size=style_profile.get("size", ""),
        background=style_profile.get("background", ""),
        color_theme=style_profile.get("color_theme", "")
    )

    return {
        "asset_id": asset.get("asset_id"),
        "asset_type": asset_type,
        "display_name": asset.get("display_name"),
        "prompt": prompt,
        "negative_prompt": template.get("negative_prompt", "")
    }


def compose_prompts(asset_list: List[dict], style_profile: dict) -> List[dict]:
    """Compose prompts for selected assets."""
    results = []

    for asset in asset_list:
        if asset.get("selected", True):
            results.append(compose_prompt(asset, style_profile))

    return results
