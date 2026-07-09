from engine.qc import run_prompt_qc


def test_qc_returns_all_core_items():
    result = run_prompt_qc(
        {
            "prompt": "Scene: Luxury glass interior. Motion: Fireplace hero motion.",
            "negative_prompt": "no morphing, no camera movement, no lighting flicker",
        }
    )

    item_names = {item["item"] for item in result}

    assert "Prompt Detection" in item_names
    assert "Artifact" in item_names
    assert "Loop" in item_names
    assert "Reflection" in item_names
    assert all(item["status"] in {"PASS", "WARNING", "FAIL"} for item in result)

