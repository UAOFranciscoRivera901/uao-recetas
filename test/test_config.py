from src.models.config import MODEL_OPTIONS, CONFIG_MODEL

def test_model_options():
    """Verifica que MODEL_OPTIONS contiene los modelos TinyLlama y GPT-2."""
    assert "TinyLlama" in MODEL_OPTIONS
    assert "GPT-2-small" in MODEL_OPTIONS

def test_config_model():
    """Verifica que CONFIG_MODEL tiene los valores esperados para los modelos."""
    assert CONFIG_MODEL["max_length"] == 500
    assert CONFIG_MODEL["temperature"] == 0.5
    assert CONFIG_MODEL["top_p"] == 0.9
    assert CONFIG_MODEL["repetition_penalty"] == 1.2
    assert CONFIG_MODEL["do_sample"] is True