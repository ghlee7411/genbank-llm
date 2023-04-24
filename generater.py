# [Sources]
# https://github.com/Stability-AI/StableLM/blob/main/notebooks/stablelm-alpha.ipynb
# https://huggingface.co/stabilityai/stablelm-tuned-alpha-3b

from transformers import AutoTokenizer, AutoModelForCausalLM


def cprint(msg: str, color: str = "blue", **kwargs) -> str:
    if color == "blue": print("\033[34m" + msg + "\033[0m", **kwargs)
    elif color == "red": print("\033[31m" + msg + "\033[0m", **kwargs)
    elif color == "green": print("\033[32m" + msg + "\033[0m", **kwargs)
    elif color == "yellow": print("\033[33m" + msg + "\033[0m", **kwargs)
    elif color == "purple": print("\033[35m" + msg + "\033[0m", **kwargs)
    elif color == "cyan": print("\033[36m" + msg + "\033[0m", **kwargs)
    else: raise ValueError(f"Invalid info color: `{color}`")


model_name = "stabilityai/stablelm-tuned-alpha-3b" 
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_text(prompt: str, max_length: int = 100, **kwargs) -> str:
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(input_ids, max_length=max_length, **kwargs)
    return tokenizer.decode(output[0], skip_special_tokens=True)
