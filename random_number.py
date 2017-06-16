from flask import Flask, render_template
from flask_ask import Ask, statement
import random

app = Flask(__name__)
ask = Ask(app, '/')

@ask.intent('RandomNumber', convert={'lowerLimit': int, 'upperLimit': int})
def hello(lowerLimit, upperLimit):
	if lowerLimit == None:
		lowerLimit = 0
	if upperLimit == None:
		upperLimit = 100
	number = random.randint(lowerLimit, upperLimit)
	text = render_template('random_number', lowerLimit=lowerLimit, upperLimit=upperLimit, number=number)
	return statement(text).simple_card('Flask-Ask Random Number', text)

if __name__ == '__main__':
    app.run(debug=True)