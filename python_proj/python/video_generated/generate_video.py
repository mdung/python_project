import openai

# Set your OpenAI API key
api_key = "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"

def generate_video(prompt):
    # Set parameters for GPT API call
    model = "text-davinci-003"  # Use a suitable model
    temperature = 0.7  # Adjust the temperature based on your preference (higher values for more randomness)

    # Initialize OpenAI API client
    openai.api_key = api_key

    # Generate text from prompt using OpenAI GPT API
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=temperature,
        n=1,  # Number of responses to generate
    )

    # Extract the generated text from the response
    generated_text = response.choices[0].text.strip()

    # You can now use the generated text to create a video using video editing tools or other services.
    print("Generated Text:", generated_text)

if __name__ == "__main__":
    # Example prompt
    prompt = "Create a video showing a journey through a fantasy world with magical creatures."

    generate_video(prompt)
