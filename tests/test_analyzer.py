from engine.analyzer import analyze_text


def test_analyze_text_detects_core_visual_dna():
    result = analyze_text(
        "Ultra luxury penthouse in Rome at night with fireplace, glass, warm tungsten lighting, cinematic cinemagraph."
    )

    assert result["input_type"] == "text"
    assert result["background_profile"]["has_interior"] is True
    assert result["background_profile"]["has_night"] is True
    assert result["dna_summary"]["world"] == "Luxury Interior"
    assert result["dna_summary"]["motion"] == "Fireplace Hero Motion"
    assert result["theme_mapping"]["theme_name"] != "Unmapped Visual Theme"
    assert result["risk_detection"]


def test_analyze_empty_input_returns_stable_shape():
    result = analyze_text("")

    assert result["normalized_input"] == ""
    assert "background_profile" in result
    assert "dna_detection" in result
    assert "dna_summary" in result
    assert "theme_mapping" in result
    assert "risk_detection" in result

