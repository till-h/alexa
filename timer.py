from flask import Flask, render_template
from flask_ask import Ask, statement
import random
import time

app = Flask(__name__)
ask = Ask(app, '/')

@ask.intent('Timekeeper')
def time_presentation():
	print('Hello')
	time.sleep(2)
	print('Hola')
	time.sleep(4)
	print('Over!')

	text = render_template('timer')
	return statement(text).simple_card('Timekeeper', text)

if __name__ == '__main__':
    app.run(debug=True)