import pytest
from src.models.model import cargar_modelo

def test_cargar_modelo_ficticio():
    # Capturar la excepcion mediante raises
    # Porque se va a cargar un modelo ficticio
    with pytest.raises(OSError):
        model_name = "modelo_ficticio"
        cargar_modelo(model_name)