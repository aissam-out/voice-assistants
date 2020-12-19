from flask import Flask
from flask_ask import Ask, statement, question, session
import jsonify
import requests
import time
import unidecode
from alexa_emails import alexa_mail 

app = Flask(__name__)
ask = Ask(app, "/mailexa")

@app.route("/")
def hello():
    return "Hello, World!"

@ask.launch
def start_skill():
    welcome_message = "Hello there, I am here to help you send emails easily .."
    return question(welcome_message)

@ask.intent('remainder', mapping={'name': 'name'})
def send_remainder(name):
    try:
        answer = alexa_mail(name, 'remainder')
    except:
        answer = "Error !"
    return statement(answer)


@ask.intent('assistance', mapping={'name': 'name'})
def send_remainder(name):
    try:
        answer = alexa_mail(name, 'assistance')
    except:
        answer = "Error !"
    return statement(answer)

@ask.intent('absence', mapping={'name': 'name'})
def send_remainder(name):
    try:
        answer = alexa_mail(name, 'absence')
    except:
        answer = "Error !"
    return statement(answer)

if __name__ == "__main__":
    app.run(debug=True)
