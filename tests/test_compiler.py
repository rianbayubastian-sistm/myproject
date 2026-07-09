from engine.compiler import compile_prompt


def test_compile_prompt_returns_prompt_negative_and_version():
    scene = {
        "scene": "Luxury penthouse in Rome.",
        "camera": "38 mm eye-level architectural perspective.",
        "lighting": "Warm tungsten interior lighting.",
        "material": "Glass, walnut, oak, crystal.",
        "motion": "Fireplace hero motion only.",
        "boundary": "Absolute positional stability.",
    }

    result = compile_prompt(scene)

    assert "Luxury penthouse" in result["prompt"]
    assert "no camera movement" in result["negative_prompt"]
    assert result["format"] == "MP4"
    assert result["duration_seconds"] == 5
    assert result["version"] == "0.1.0"


def test_compile_prompt_respects_custom_output_metadata():
    scene = {
        "scene": "Beach cafe rain.",
        "format": "GIF",
        "duration_seconds": 3,
        "negative": "no jitter",
    }

    result = compile_prompt(scene)

    assert result["format"] == "GIF"
    assert result["duration_seconds"] == 3
    assert result["negative_prompt"] == "no jitter"

