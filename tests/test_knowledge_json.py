import json
from pathlib import Path


def test_all_knowledge_json_files_are_valid():
    root = Path(__file__).resolve().parents[1]
    knowledge_dir = root / "knowledge"

    json_files = list(knowledge_dir.glob("*.json"))

    assert json_files
    for path in json_files:
        data = json.loads(path.read_text(encoding="utf-8"))
        assert isinstance(data, list)


def test_settings_json_has_frozen_menu():
    root = Path(__file__).resolve().parents[1]
    settings = json.loads((root / "config" / "settings.json").read_text(encoding="utf-8"))

    assert settings["app_name"] == "VGOS"
    assert settings["version"] == "0.1.0"
    assert len(settings["frozen_menu"]) == 10

