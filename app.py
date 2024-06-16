from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

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
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I am having trouble understanding you. Please try again."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']
    response = get_response(user_input)
    return {
        "user_input": user_input,
        "response": response
    }

if __name__ == '__main__':
    app.run(debug=True)
