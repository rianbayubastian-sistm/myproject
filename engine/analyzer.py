from __future__ import annotations

from typing import Any

from .dna_detector import build_dna_summary, detect_dna
from .normalizer import normalize_prompt_text
from .theme_mapper import map_theme


def detect_background(text: str) -> dict[str, Any]:
    lowered = text.lower()
    return {
        "has_interior": any(word in lowered for word in ["interior", "room", "apartment", "penthouse", "cafe"]),
        "has_exterior": any(word in lowered for word in ["skyline", "city", "beach", "street", "outdoor"]),
        "has_night": any(word in lowered for word in ["night", "nocturnal", "evening"]),
    }


def detect_risk(text: str) -> list[dict[str, str]]:
    lowered = text.lower()
    risks = []
    if any(word in lowered for word in ["cinemagraph", "loop", "gif", "flame", "fire"]):
        risks.append({"level": "WARNING", "item": "Temporal consistency", "note": "Gerakan perlu dikunci agar tidak terjadi morphing atau flicker."})
    if any(word in lowered for word in ["glass", "reflection", "crystal"]):
        risks.append({"level": "WARNING", "item": "Reflection", "note": "Refleksi kaca perlu dijaga stabil antar-frame."})
    if not risks:
        risks.append({"level": "PASS", "item": "General", "note": "Belum ada risiko spesifik dari input teks."})
    return risks


def analyze_text(text: str) -> dict[str, Any]:
    normalized = normalize_prompt_text(text)
    detections = detect_dna(normalized)
    dna_summary = build_dna_summary(detections)

    return {
        "input_type": "text",
        "normalized_input": normalized,
        "background_profile": detect_background(normalized),
        "dna_detection": detections,
        "dna_summary": dna_summary,
        "theme_mapping": map_theme(dna_summary),
        "risk_detection": detect_risk(normalized),
    }


def analyze_image_metadata(file_name: str, content_type: str | None, file_size: int) -> dict[str, Any]:
    text_seed = file_name.replace("_", " ").replace("-", " ")
    result = analyze_text(text_seed)
    result["input_type"] = "image"
    result["image_profile"] = {
        "file_name": file_name,
        "content_type": content_type or "unknown",
        "file_size_bytes": file_size,
        "note": "MVP 0.1.0 memakai metadata file dan nama file sebagai seed analisis. Computer vision dapat ditambahkan pada milestone berikutnya.",
    }
    return result

