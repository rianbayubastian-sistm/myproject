from __future__ import annotations

from typing import Any


def map_theme(dna_summary: dict[str, Any]) -> dict[str, Any]:
    world = dna_summary.get("world", "Unknown")
    weather = dna_summary.get("weather", "Unknown")
    lighting = dna_summary.get("lighting", "Unknown")
    architecture = dna_summary.get("architecture", "Unknown")

    theme_parts = [part for part in [world, architecture, weather, lighting] if part != "Unknown"]
    theme_name = " / ".join(theme_parts) if theme_parts else "Unmapped Visual Theme"

    return {
        "theme_name": theme_name,
        "world": world,
        "weather": weather,
        "lighting": lighting,
        "architecture": architecture,
    }

