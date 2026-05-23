import json
from pathlib import Path
from typing import Dict, List


STYLE_TEMPLATE_PATH = Path("data/style_templates.json")


def load_style_templates() -> Dict[str, dict]:
    """Load style templates from JSON."""
    if not STYLE_TEMPLATE_PATH.exists():
        return {}

    with STYLE_TEMPLATE_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def get_style_names() -> List[str]:
    """Return available style display names."""
    styles = load_style_templates()
    return list(styles.keys())


def build_style_profile(
    style_name: str,
    size: str,
    view: str,
    background: str,
    color_theme: str
) -> dict:
    """Build a style profile for consistent asset generation."""
    styles = load_style_templates()
    template = styles.get(style_name, {})

    return {
        "style_name": style_name,
        "style_key": template.get("style_key", style_name),
        "style_prompt": template.get("style_prompt", ""),
        "size": size,
        "view": view,
        "background": background,
        "color_theme": color_theme
    }
