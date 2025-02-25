import pytest
from src.models.model import cargar_modelo
from src.models.config import MODEL_OPTIONS

def test_cargar_modelo_ficticio():
    """Verifica que cargar_modelo lanza un error al usar un modelo inexistente."""
    with pytest.raises(OSError):
        model_name = "modelo_ficticio"
        cargar_modelo(model_name)

def test_cargar_modelo():
    """Verifica que cargar_modelo sea satisfactorio para el modelo TinyLlama."""
    model_name = MODEL_OPTIONS["TinyLlama"]
    tokenizer, model, device = cargar_modelo(model_name)
    
    # Verificar que el tokenizador y el modelo no son None
    assert tokenizer is not None, "El tokenizador no se cargó correctamente"
    assert model is not None, "El modelo no se cargó correctamente"
    
    # Verificar que el tipo del dispositivo es cpu
    assert device.type == 'cpu', "El tipo de dispositivo no es cpu"