from __future__ import annotations


QC_ITEMS = [
    "Prompt Detection",
    "Artifact",
    "Loop",
    "Reflection",
    "Geometry",
    "Identity",
    "Resolution",
    "Overlay",
    "Channel Identity",
]


def run_prompt_qc(compiled_prompt: dict) -> list[dict[str, str]]:
    prompt = compiled_prompt.get("prompt", "")
    negative = compiled_prompt.get("negative_prompt", "")
    results = []

    for item in QC_ITEMS:
        status = "PASS"
        note = "No issue detected in MVP rule check."
        if item == "Loop" and "motion" not in prompt.lower():
            status = "WARNING"
            note = "Motion belum jelas untuk output loop."
        if item == "Artifact" and "morphing" not in negative.lower():
            status = "WARNING"
            note = "Negative prompt belum menjaga morphing."
        if item == "Reflection" and "glass" in prompt.lower() and "reflection" not in negative.lower():
            status = "WARNING"
            note = "Refleksi disebut, tetapi guard refleksi belum eksplisit."
        results.append({"item": item, "status": status, "note": note})

    return results

