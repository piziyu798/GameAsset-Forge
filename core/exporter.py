import json
import shutil
import zipfile
from datetime import datetime
from pathlib import Path
from typing import List


OUTPUT_DIR = Path("outputs")
EXPORT_ROOT = OUTPUT_DIR / "asset_pack"
ZIP_PATH = OUTPUT_DIR / "asset_pack.zip"


TYPE_TO_FOLDER = {
    "character": "characters",
    "enemy": "enemies",
    "item": "items",
    "tile": "tiles",
    "ui": "ui",
    "background": "backgrounds",
    "other": "others"
}


def clean_export_dir() -> None:
    """Clean previous export output."""
    OUTPUT_DIR.mkdir(exist_ok=True)

    if EXPORT_ROOT.exists():
        shutil.rmtree(EXPORT_ROOT)

    if ZIP_PATH.exists():
        ZIP_PATH.unlink()

    EXPORT_ROOT.mkdir(parents=True, exist_ok=True)


def safe_filename(text: str) -> str:
    """Create a simple safe filename."""
    if not text:
        return "unnamed_asset"

    replacements = {
        " ": "_",
        "/": "_",
        "\\": "_",
        ":": "_",
        "*": "_",
        "?": "_",
        "\"": "_",
        "<": "_",
        ">": "_",
        "|": "_"
    }

    result = text.strip()
    for old, new in replacements.items():
        result = result.replace(old, new)

    return result


def copy_asset_files(assets: List[dict]) -> List[dict]:
    """Copy image files into export folder and build manifest records."""
    manifest = []

    for index, asset in enumerate(assets, start=1):
        asset_type = asset.get("asset_type", "other")
        folder = TYPE_TO_FOLDER.get(asset_type, "others")

        src_path = Path(asset.get("image_path", ""))
        if not src_path.exists():
            continue

        target_dir = EXPORT_ROOT / folder
        target_dir.mkdir(parents=True, exist_ok=True)

        file_name = f"{index:03d}_{safe_filename(asset.get('display_name', 'asset'))}.png"
        target_path = target_dir / file_name

        shutil.copy2(src_path, target_path)

        manifest.append({
            "asset_id": asset.get("asset_id"),
            "asset_type": asset_type,
            "display_name": asset.get("display_name"),
            "description_zh": asset.get("description_zh", ""),
            "file_path": str(target_path.relative_to(EXPORT_ROOT)),
            "generation_mode": asset.get("generation_mode"),
            "match_strategy": asset.get("match_strategy"),
            "demo_display_name": asset.get("demo_display_name"),
            "prompt": asset.get("prompt", ""),
            "negative_prompt": asset.get("negative_prompt", "")
        })

    return manifest


def write_manifest(manifest: List[dict]) -> None:
    """Write manifest.json."""
    manifest_path = EXPORT_ROOT / "manifest.json"

    with manifest_path.open("w", encoding="utf-8") as f:
        json.dump(
            {
                "exported_at": datetime.now().isoformat(timespec="seconds"),
                "asset_count": len(manifest),
                "assets": manifest
            },
            f,
            ensure_ascii=False,
            indent=2
        )


def write_readme(manifest: List[dict]) -> None:
    """Write README.md for exported asset pack."""
    readme_path = EXPORT_ROOT / "README.md"

    lines = [
        "# GameAsset Forge 导出素材包",
        "",
        "本素材包由 GameAsset Forge Demo Mode 生成，用于展示 2D 游戏素材工作流。",
        "",
        "## 目录说明",
        "",
        "- characters/：角色素材",
        "- enemies/：敌人素材",
        "- items/：道具素材",
        "- tiles/：地图块素材",
        "- ui/：UI 素材",
        "- backgrounds/：背景素材",
        "- manifest.json：素材元数据与 Prompt 记录",
        "",
        "## 素材列表",
        ""
    ]

    for item in manifest:
        lines.append(
            f"- {item.get('display_name')} | 类型：{item.get('asset_type')} | 文件：{item.get('file_path')}"
        )

    lines.extend([
        "",
        "## 说明",
        "",
        "当前导出结果来自 Demo Mode 的内置示例素材池。若需要与 Prompt 高度一致的真实图片，可在后续 API Mode 中调用图像生成模型。"
    ])

    readme_path.write_text("\n".join(lines), encoding="utf-8")


def zip_export_dir() -> Path:
    """Zip export folder."""
    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file_path in EXPORT_ROOT.rglob("*"):
            if file_path.is_file():
                zipf.write(file_path, file_path.relative_to(OUTPUT_DIR))

    return ZIP_PATH


def export_asset_pack(assets: List[dict]) -> Path:
    """Export generated assets as a zip package."""
    clean_export_dir()
    manifest = copy_asset_files(assets)
    write_manifest(manifest)
    write_readme(manifest)
    return zip_export_dir()
