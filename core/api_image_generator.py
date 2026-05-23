import base64
import json
import time
from pathlib import Path
from typing import Dict, List

import requests


OUTPUT_DIR = Path("outputs/api_generated")


def ensure_output_dir() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def safe_filename(text: str) -> str:
    if not text:
        return "asset"

    result = str(text).strip()
    for ch in [" ", "/", "\\", ":", "*", "?", "\"", "<", ">", "|", "\n", "\t"]:
        result = result.replace(ch, "_")

    return result[:80]


def normalize_base_url(base_url: str) -> str:
    base_url = str(base_url or "").strip().rstrip("/")
    if not base_url:
        raise ValueError("API Base URL 不能为空")

    if base_url.endswith("/images/generations"):
        return base_url

    return f"{base_url}/images/generations"


def is_siliconflow_url(base_url: str) -> bool:
    base_url = str(base_url or "").lower()
    return "siliconflow" in base_url


def save_b64_image(b64_data: str, output_path: Path) -> None:
    image_bytes = base64.b64decode(b64_data)
    output_path.write_bytes(image_bytes)


def download_image(image_url: str, output_path: Path) -> None:
    response = requests.get(image_url, timeout=120)
    response.raise_for_status()
    output_path.write_bytes(response.content)


def build_payload(
    prompt: str,
    base_url: str,
    model: str,
    size: str = "1024x1024"
) -> Dict[str, object]:
    """
    Build provider-specific image generation payload.

    SiliconFlow uses:
    - image_size
    - batch_size
    - num_inference_steps
    - guidance_scale

    OpenAI-style image APIs usually use:
    - size
    - n
    - response_format
    """
    if is_siliconflow_url(base_url):
        return {
            "model": model,
            "prompt": prompt,
            "image_size": size,
            "batch_size": 1,
            "num_inference_steps": 20,
            "guidance_scale": 7.5
        }

    return {
        "model": model,
        "prompt": prompt,
        "size": size,
        "n": 1,
        "response_format": "b64_json"
    }


def extract_first_image_result(result: Dict[str, object]) -> Dict[str, object]:
    """
    Support both SiliconFlow and OpenAI-style image generation responses.

    SiliconFlow often returns:
    {
      "images": [{"url": "..."}]
    }

    OpenAI-style providers often return:
    {
      "data": [{"b64_json": "..."}]
    }
    or:
    {
      "data": [{"url": "..."}]
    }
    """
    if "images" in result and result["images"]:
        return result["images"][0]

    if "data" in result and result["data"]:
        return result["data"][0]

    raise RuntimeError(f"API 返回格式异常：{result}")


def call_image_generation_api(
    prompt: str,
    api_key: str,
    base_url: str,
    model: str,
    size: str = "1024x1024"
) -> Dict[str, object]:
    endpoint = normalize_base_url(base_url)

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = build_payload(
        prompt=prompt,
        base_url=base_url,
        model=model,
        size=size
    )

    response = requests.post(
        endpoint,
        headers=headers,
        data=json.dumps(payload),
        timeout=180
    )

    if response.status_code >= 400:
        raise RuntimeError(f"API 调用失败：{response.status_code} - {response.text[:500]}")

    result = response.json()
    return extract_first_image_result(result)


def select_assets_balanced_by_type(asset_list: List[dict], max_assets: int) -> List[dict]:
    """
    Select assets in a balanced way across asset types.

    This avoids API Mode only generating the first several assets,
    which are often all characters.
    """
    type_order = ["character", "enemy", "item", "tile", "ui", "background", "other"]
    grouped = {asset_type: [] for asset_type in type_order}

    for asset in asset_list:
        if not asset.get("selected", True):
            continue

        asset_type = asset.get("asset_type", "other")
        if asset_type not in grouped:
            asset_type = "other"

        grouped[asset_type].append(asset)

    selected = []

    while len(selected) < max_assets:
        added_this_round = False

        for asset_type in type_order:
            if len(selected) >= max_assets:
                break

            if grouped[asset_type]:
                selected.append(grouped[asset_type].pop(0))
                added_this_round = True

        if not added_this_round:
            break

    return selected


def generate_api_assets(
    asset_list: List[dict],
    prompts: List[dict],
    api_key: str,
    base_url: str,
    model: str,
    size: str = "1024x1024",
    max_assets: int = 6
) -> List[dict]:
    """
    Generate images through API Mode and return records compatible with Demo Mode gallery/export.
    """
    if not api_key:
        raise ValueError("API Key 不能为空")

    if not model:
        raise ValueError("模型名称不能为空")

    ensure_output_dir()

    prompt_map = {
        item.get("asset_id"): item
        for item in prompts
    }

    selected_assets = select_assets_balanced_by_type(
        asset_list=asset_list,
        max_assets=max_assets
    )

    results = []

    for index, asset in enumerate(selected_assets, start=1):
        asset_id = asset.get("asset_id", f"api_{index:03d}")
        prompt_record = prompt_map.get(asset_id, {})
        prompt = prompt_record.get("prompt", "")

        if not prompt:
            prompt = asset.get("description_zh") or asset.get("display_name", "")

        output_name = f"{index:03d}_{safe_filename(asset.get('display_name', asset_id))}.png"
        output_path = OUTPUT_DIR / output_name

        api_result = call_image_generation_api(
            prompt=prompt,
            api_key=api_key,
            base_url=base_url,
            model=model,
            size=size
        )

        if api_result.get("b64_json"):
            save_b64_image(api_result["b64_json"], output_path)
        elif api_result.get("url"):
            download_image(api_result["url"], output_path)
        else:
            raise RuntimeError(f"API 返回中没有 b64_json 或 url：{api_result}")

        results.append(
            {
                "asset_id": asset_id,
                "asset_type": asset.get("asset_type", "other"),
                "display_name": asset.get("display_name", "未命名素材"),
                "description_zh": asset.get("description_zh", ""),
                "image_path": str(output_path),
                "match_strategy": "API 生成",
                "demo_display_name": "真实 API 生成",
                "generation_mode": "API Mode",
                "prompt": prompt,
                "negative_prompt": prompt_record.get("negative_prompt", "")
            }
        )

        time.sleep(0.2)

    return results
