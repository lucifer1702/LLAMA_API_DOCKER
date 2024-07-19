from transformers import LlamaForCausalLM, LlamaTokenizer


# Load model and tokenizer
def llama_model(model_name: str):
    model = LlamaForCausalLM.from_pretrained(model_name)
    tokenizer = LlamaTokenizer.from_pretrained(model_name)
    return model, tokenizer
