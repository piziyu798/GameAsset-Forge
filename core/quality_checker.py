from pathlib import Path
from typing import List, Dict


REQUIRED_FIELDS = [
    "asset_id",
    "asset_type",
    "display_name",
    "image_path",
    "generation_mode",
    "match_strategy"
]


def check_asset_quality(asset: dict) -> dict:
    """Check whether one generated asset is usable for export."""
    issues = []
    warnings = []

    for field in REQUIRED_FIELDS:
        if not asset.get(field):
            issues.append(f"缺少必要字段：{field}")

    image_path = asset.get("image_path", "")
    if image_path and not Path(image_path).exists():
        issues.append("图片文件不存在")

    if asset.get("match_strategy") in {"同类型替代", "全局替代"}:
        warnings.append("该素材未精准匹配，当前使用 Demo 替代素材")

    if not asset.get("prompt"):
        warnings.append("缺少 Prompt 记录")

    status = "通过" if not issues else "未通过"

    return {
        "asset_id": asset.get("asset_id", ""),
        "display_name": asset.get("display_name", "未命名素材"),
        "asset_type": asset.get("asset_type", "other"),
        "status": status,
        "issues": "；".join(issues) if issues else "无",
        "warnings": "；".join(warnings) if warnings else "无"
    }


def check_assets_quality(assets: List[dict]) -> Dict[str, object]:
    """Check all generated assets and return summary."""
    details = [check_asset_quality(asset) for asset in assets]

    total = len(details)
    passed = sum(1 for item in details if item["status"] == "通过")
    failed = total - passed

    warning_count = sum(
        1 for item in details
        if item["warnings"] and item["warnings"] != "无"
    )

    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "warning_count": warning_count,
        "details": details
    }
