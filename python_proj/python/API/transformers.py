from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_text(prompt, model_name='gpt2', max_tokens=100):
    """
    Generate text using the Hugging Face Transformers library.

    Args:
        prompt (str): The prompt for text generation.
        model_name (str): The pre-trained model name (e.g., 'gpt2').
        max_tokens (int): The maximum number of tokens to generate.

    Returns:
        str: The generated text.
    """
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(**inputs, max_length=max_tokens, num_return_sequences=1)

    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text

def main():
    # Example usage
    prompt_text = input("Enter a prompt for text generation: ")
    generated_text = generate_text(prompt_text, model_name='gpt2')

    print("\nGenerated Text:")
    print(generated_text)

if __name__ == "__main__":
    main()
