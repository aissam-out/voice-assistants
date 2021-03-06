from flask import Flask
from flask_ask import Ask, statement, question, session
import jsonify
import requests
import time
import unidecode
from alexa_emails import alexa_mail

app = Flask(__name__)
ask = Ask(app, "/mailexa")

# A 'hello world' message in the / route - just for test
@app.route("/")
def hello():
    return "Hello, World!"

# the welcome message said by alexa when the application is called
@ask.launch
def start_skill():
    welcome_message = "Hello there, I am here to help you send emails easily .."
    # 'question' in the following line will expect a response/ an entry from the
    # client
    return question(welcome_message)

# if the intent 'remainder' is detected, send an appropriate email
@ask.intent('remainder', mapping={'name': 'name'})
def send_remainder(name):
    try:
        answer = alexa_mail(name, 'remainder')
    except:
        answer = "Error !"
    return statement(answer)

# if the intent 'assistance' is detected, send an appropriate email
@ask.intent('assistance', mapping={'name': 'name'})
def send_remainder(name):
    try:
        answer = alexa_mail(name, 'assistance')
    except:
        answer = "Error !"
    return statement(answer)

# if the intent 'absence' is detected, send an appropriate email
@ask.intent('absence', mapping={'name': 'name'})
def send_remainder(name):
    try:
        answer = alexa_mail(name, 'absence')
    except:
        answer = "Error !"
    return statement(answer)

if __name__ == "__main__":
    app.run(debug=True)
