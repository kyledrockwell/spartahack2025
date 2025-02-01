import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Replace with your OpenRouter API key

API_KEY = "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"
OPENROUTER_URL="https://openrouter.ai/api/v1/chat/completions"

prompt = ""
with open("./flask/prompts/cse320.txt", 'r') as file:
    prompt = file.read()

@app.route("/ai", methods=["GET", "POST"])
def index():
    response_text = None

    if request.method == "POST":
        user_message = request.form.get("message")  # Get input from form

        # Prepare the request payload
        headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
        payload = {
            "model": "openai/gpt-3.5-turbo",  # Choose a model from OpenRouter
            "messages": [{"role": "user", "content": prompt + " " + user_message}]
        }

        # Make the API request
        response = requests.post(OPENROUTER_URL, json=payload, headers=headers)

        # Handle the response
        if response.status_code == 200:
            response_text = response.json()["choices"][0]["message"]["content"]
        else:
            response_text = f"Error: {response.text}"

    return render_template("ai.html", response_text=response_text)

if __name__ == "__main__":
    app.run(debug=True)
