from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float32,   # CPU SAFE
)

def run_llm(prompt: str) -> str:
    inputs = tokenizer(prompt, return_tensors="pt")
    output = model.generate(
        **inputs,
        max_new_tokens=200,
        temperature=0.7
    )
    return tokenizer.decode(output[0], skip_special_tokens=True)
