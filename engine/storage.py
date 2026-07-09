from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT_DIR = Path(__file__).resolve().parents[1]
KNOWLEDGE_DIR = ROOT_DIR / "knowledge"
PROJECTS_DIR = ROOT_DIR / "projects"


def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def load_knowledge(name: str) -> list[dict[str, Any]]:
    return read_json(KNOWLEDGE_DIR / f"{name}.json", [])


def list_projects() -> list[dict[str, Any]]:
    PROJECTS_DIR.mkdir(parents=True, exist_ok=True)
    projects = []
    for path in sorted(PROJECTS_DIR.glob("*.json")):
        projects.append(read_json(path, {}))
    return projects


def project_path(project_id: str) -> Path:
    safe_id = "".join(char for char in project_id.lower().replace(" ", "_") if char.isalnum() or char == "_")
    return PROJECTS_DIR / f"{safe_id}.json"


def save_project(project: dict[str, Any]) -> None:
    write_json(project_path(project["id"]), project)

