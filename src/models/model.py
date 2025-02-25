from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from src.models.config import CONFIG_MODEL

def cargar_modelo(model_name):
    """Carga el modelo y el tokenizador para generación de texto."""
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    device = torch.device("cpu")
    model.to(device)
    return tokenizer, model, device

def generar_receta(ingredientes, model_name):
    """Genera una receta en base a los ingredientes proporcionados."""
    tokenizer, model, device = cargar_modelo(model_name)
    
    prompt = ("""
    Genera una receta usando los siguientes ingredientes: {ingredientes}.
    
    Ejemplo de formato:
    
    Ingredientes:
    - Pollo
    - Arroz
    - Cebolla
    
    Nombre: Arroz con pollo
    
    Pasos:
    1. Cocinar el arroz en agua hirviendo con sal hasta que esté suave.
    2. En una sartén, saltear la cebolla picada hasta que esté dorada.
    3. Agregar el pollo troceado y cocinar hasta que esté bien cocido.
    4. Mezclar el arroz con el pollo y la cebolla, y servir caliente.
    
    Ahora genera la receta con estos ingredientes:
    
    Ingredientes:
    - {ingredientes}
    
    Pasos:""").format(ingredientes=", ".join(ingredientes))
    
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    output = model.generate(
        **inputs,
        eos_token_id=tokenizer.eos_token_id,
        **CONFIG_MODEL
    )
    
    receta = tokenizer.decode(output[0], skip_special_tokens=True)
    return receta[len(prompt):].strip()
