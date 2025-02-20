from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from config import Config_Model,MODEL_OPTIONS

def cargar_modelo(model_name):
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    device = "cpu"
    model.to(device)
    
    return tokenizer, model, device

def generar_receta(ingredientes, model_name):
    
    tokenizer, model, device = cargar_modelo(model_name)
        
    prompt = f"""Genera una receta usando los siguientes ingredientes: {", ".join(ingredientes)}.

Ejemplo de formato:

Ingredientes:
- Pollo
- Arroz
- Cebolla

nombre: arroz con pollo

Pasos:
1. Cocinar el arroz en agua hirviendo con sal hasta que esté suave.
2. En una sartén, saltear la cebolla picada hasta que esté dorada.
3. Agregar el pollo troceado y cocinar hasta que esté bien cocido.
4. Mezclar el arroz con el pollo y la cebolla, y servir caliente.

Ahora genera la receta con estos ingredientes:

Ingredientes:
- {", ".join(ingredientes)}

Pasos:"""

    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    output = model.generate(
        **inputs,
        eos_token_id=tokenizer.eos_token_id,
        **Config_Model
    )

    receta = tokenizer.decode(output[0], skip_special_tokens=True)
    
    receta_generada = receta[len(prompt):].strip()
    return receta_generada