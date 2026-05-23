import json
from pathlib import Path
from typing import Dict, List


BLUEPRINT_PATH = Path("data/asset_blueprints.json")


def load_blueprints() -> Dict[str, List[dict]]:
    """Load asset blueprint templates from JSON."""
    if not BLUEPRINT_PATH.exists():
        return {}

    with BLUEPRINT_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def get_game_types() -> List[str]:
    """Return available game types."""
    blueprints = load_blueprints()
    return list(blueprints.keys())


def generate_asset_blueprint(game_type: str) -> List[dict]:
    """Generate recommended asset list by game type."""
    blueprints = load_blueprints()
    assets = blueprints.get(game_type, [])

    result = []
    for index, asset in enumerate(assets, start=1):
        result.append(
            {
                "asset_id": f"asset_{index:03d}",
                "asset_type": asset.get("asset_type", "other"),
                "display_name": asset.get("display_name", "未命名素材"),
                "description_zh": asset.get("description_zh", ""),
                "selected": True,
                "status": "pending"
            }
        )

    return result
