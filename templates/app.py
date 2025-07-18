from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hello! How can I help you?"
    elif "your name" in user_input or "who are you" in user_input:
        return "I am your AI chatbot."
    elif "python" in user_input:
        return "Python is a powerful programming language used for AI."
    elif "joke" in user_input or "funny" in user_input or "laugh" in user_input:
        return get_joke()
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand."

def get_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return data["joke"]
    except:
        return "Sorry, I couldn't fetch a joke right now."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_bot_response():
    user_input = request.args.get('msg')
    return get_response(user_input)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
