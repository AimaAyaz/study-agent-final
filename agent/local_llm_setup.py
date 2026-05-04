from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load TinyLlama model
MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16,
    device_map="auto"
)

def run_llm(prompt: str) -> str:
    """Generate text using the local LLM."""
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    output = model.generate(
        **inputs,
        max_new_tokens=200,
        temperature=0.7
    )
    return tokenizer.decode(output[0], skip_special_tokens=True)
