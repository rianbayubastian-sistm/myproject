from __future__ import annotations


def normalize_prompt_text(text: str) -> str:
    return " ".join(text.strip().split())


def normalize_scene(scene: dict) -> dict:
    normalized = {}
    for key, value in scene.items():
        if isinstance(value, str):
            normalized[key] = normalize_prompt_text(value)
        elif isinstance(value, list):
            normalized[key] = [normalize_prompt_text(str(item)) for item in value if str(item).strip()]
        else:
            normalized[key] = value
    return normalized

