from __future__ import annotations

from .normalizer import normalize_scene


SECTION_ORDER = [
    "scene",
    "camera",
    "lighting",
    "weather",
    "material",
    "motion",
    "boundary",
    "decoration",
    "overlay",
]


def compile_prompt(scene: dict) -> dict:
    normalized = normalize_scene(scene)
    parts = []
    for key in SECTION_ORDER:
        value = normalized.get(key)
        if value:
            label = key.replace("_", " ").title()
            parts.append(f"{label}: {value}")

    prompt = ". ".join(parts).strip()
    if prompt and not prompt.endswith("."):
        prompt += "."

    negative = normalized.get(
        "negative",
        "no camera movement, no parallax drift, no morphing, no melting, no warping, no lighting flicker, no compression artifacts, no unstable geometry",
    )

    return {
        "prompt": prompt,
        "negative_prompt": negative,
        "format": normalized.get("format", "MP4"),
        "duration_seconds": normalized.get("duration_seconds", 5),
        "version": "0.1.0",
    }

