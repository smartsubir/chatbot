import openai
import os

# Set your OpenAI API key
openai.api_key = os.getenv("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")

def get_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input},
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I am having trouble understanding you. Please try again."

def main():
    print("Chatbot: Hello! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
