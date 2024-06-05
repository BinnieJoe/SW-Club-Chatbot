from flask import Flask, render_template, request
from flask_sock import Sock
import openai, os
app = Flask(__name__)
sock = Sock(app=app)
openai.api_key = "sk-proj-NVI3qkvYhaIz1WAAFvaXT3BlbkFJdHiowJ1TmQAiEhXiZb8C"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chatbot/')
def chatbot():
    return render_template("chatbot.html", query="query", answer="answer")

@sock.route("/echo")
def echo(sock):
    model = "gpt-3.5-turbo"
    while True:

        data = sock.receive()

        messages = [{
            "role": "system",
            "content": "You are a helpful assistant."
        }, {
            "role": "user",
            "content": data
        }]
        response = openai.ChatCompletion.create(model=model, messages=messages)
        answer = response['choices'][0]['message']['content']
        sock.send(answer)

if __name__ == "__main__":
    app.run(debug=True)
    sock.init_app(app)

