import openai

def generate_image(prompt):
    # OpenAI GPT-3 API key
    api_key = "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"

    # Set up the OpenAI API key
    openai.api_key = api_key

    # Use the OpenAI API to generate an image based on the prompt
    response = openai.Completion.create(
        model="image-alpha-001",
        prompt=prompt,
        n=1,
        temperature=0.5
    )

    # Extract the generated image URL from the API response
    image_url = response['choices'][0]['text'].strip()

    return image_url

if __name__ == "__main__":
    # Get user input for the prompt
    user_prompt = input("Enter a prompt to generate an image: ")

    # Generate the image based on the user's prompt
    generated_image_url = generate_image(user_prompt)

    print(f"Generated Image URL: {generated_image_url}")
