import openai

def generate_text(prompt, api_key='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', engine='text-davinci-003', max_tokens=100):
    """
    Generate text using the OpenAI GPT-3 API.

    Args:
        prompt (str): The prompt for text generation.
        api_key (str): Your OpenAI API key.
        engine (str): The engine to use (e.g., 'text-davinci-003').
        max_tokens (int): The maximum number of tokens to generate.

    Returns:
        str: The generated text.
    """
    openai.api_key = api_key

    # Make a request to the completions endpoint
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=max_tokens
    )

    # Extract and return the generated text
    generated_text = response['choices'][0]['text']
    return generated_text

# Example usage
prompt_text = "Once upon a time in a"
generated_text = generate_text(prompt_text)
print(generated_text)
