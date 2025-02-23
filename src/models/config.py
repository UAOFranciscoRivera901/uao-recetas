"""Configuración de modelos para la generación de recetas."""

MODEL_OPTIONS = {
    "TinyLlama": "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    "GPT-2-small": "datificate/gpt2-small-spanish",
}

CONFIG_MODEL = {
    "max_length": 500,
    "temperature": 0.5,  # Reduce la aleatoriedad
    "top_p": 0.9,
    "repetition_penalty": 1.2,  # Evita repeticiones
    "do_sample": True,
}
