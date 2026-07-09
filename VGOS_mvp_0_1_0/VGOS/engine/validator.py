from __future__ import annotations


REQUIRED_SCENE_FIELDS = ["scene", "camera", "lighting", "material", "motion", "boundary"]


def validate_scene(scene: dict) -> list[dict[str, str]]:
    results = []
    for field in REQUIRED_SCENE_FIELDS:
        value = scene.get(field, "")
        if str(value).strip():
            results.append({"status": "PASS", "field": field, "message": "Field tersedia."})
        else:
            results.append({"status": "WARNING", "field": field, "message": "Field masih kosong."})
    return results

