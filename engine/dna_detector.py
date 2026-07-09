from __future__ import annotations

from typing import Any

from .storage import load_knowledge


KNOWLEDGE_MODULES = [
    "world",
    "camera",
    "weather",
    "material",
    "lighting",
    "boundary",
    "motion",
    "architecture",
    "decoration",
]


def _score_entry(text: str, entry: dict[str, Any]) -> int:
    keywords = entry.get("keywords", [])
    return sum(1 for keyword in keywords if keyword.lower() in text)


def detect_dna(text: str) -> dict[str, Any]:
    normalized = text.lower()
    detections: dict[str, Any] = {}

    for module in KNOWLEDGE_MODULES:
        matches = []
        for entry in load_knowledge(module):
            score = _score_entry(normalized, entry)
            if score:
                matches.append(
                    {
                        "id": entry.get("id"),
                        "label": entry.get("label"),
                        "score": score,
                        "prompt_terms": entry.get("prompt_terms", []),
                    }
                )
        matches.sort(key=lambda item: item["score"], reverse=True)
        detections[module] = matches

    return detections


def build_dna_summary(detections: dict[str, Any]) -> dict[str, Any]:
    summary = {}
    for module, matches in detections.items():
        if matches:
            summary[module] = matches[0]["label"]
        else:
            summary[module] = "Unknown"
    return summary

