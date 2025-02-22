from src.models.config import MODEL_OPTIONS, Config_Model

def test_model_options():
    # Verificar que MODEL_OPTIONS contenga los dos modelos Tiny y GPT-2
    assert "TinyLlama" in MODEL_OPTIONS
    assert "GPT-2-small" in MODEL_OPTIONS

def test_config_model():
    # Verificar que Config_Model tenga los valores esperados para utilizar los modelos
    assert Config_Model["max_length"] == 500
    assert Config_Model["temperature"] == 0.5
    assert Config_Model["top_p"] == 0.9
    assert Config_Model["repetition_penalty"] == 1.2
    assert Config_Model["do_sample"] is True