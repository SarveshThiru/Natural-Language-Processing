import openai
import os

# Set your API key securely via environment variable
openai.api_key = os.getenv('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')

def generate_text(prompt, max_tokens=100):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens
    )

    # Extract the generated text from the response
    generated_text = response.choices[0].message.content
    return generated_text

def main():
    prompt = input("Enter a prompt: ")
    generated_text = generate_text(prompt)

    print("\nGenerated Text:")
    print(generated_text)

if __name__ == "__main__":
    main()
