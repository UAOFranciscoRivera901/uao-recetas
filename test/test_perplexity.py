from transformers import GPT2LMHeadModel, GPT2Tokenizer, AutoModelForCausalLM, AutoTokenizer
import torch

models = {
    "GPT2-SMALL-SPANISH":{
        "model": GPT2LMHeadModel.from_pretrained("datificate/gpt2-small-spanish"),
        "tokenizer": GPT2Tokenizer.from_pretrained("datificate/gpt2-small-spanish")
    },
    
    "TINYLLAMA":{
        "model": AutoModelForCausalLM.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0"),
        "tokenizer": AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
    }
}

def calculate_perplexity(model, tokenizer,text):
    """ calcular la perplejidad de un texto usando el modelo y el tokenizador"""
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs, labels=inputs["input_ids"])
        loss = outputs.loss
    return torch.exp(loss).item()

text = "poner"

results = {name: calculate_perplexity(data["model"], data["tokenizer"], text) for name, data in models.items()}

for model_name, perplexity in results.items():
    print(f"Perplejidad con {model_name}: {perplexity:.2f}")