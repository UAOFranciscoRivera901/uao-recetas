import pytest
from src.models.model import cargar_modelo

def test_cargar_modelo_ficticio():
    """Verifica que cargar_modelo lanza un error al usar un modelo inexistente."""
    with pytest.raises(OSError, match=".*Error al cargar el modelo.*"):
        model_name = "modelo_ficticio"
        cargar_modelo(model_name)
