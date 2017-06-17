from flask import Flask, render_template
from flask_ask import Ask, statement
import time
import RPi.GPIO as GPIO

app = Flask(__name__)
ask = Ask(app, '/')

GPIO_PIN = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.OUT)

@ask.intent('GPIO')
def gpio_controller(state):
	instruction = None
	text = 'Switching LED'
	if state == None:
		instruction = not GPIO.input(GPIO_PIN)
	elif state == 'on':
		instruction = GPIO.HIGH
	elif state == 'off':
		instruction = GPIO.LOW
	else:
		text = 'Sorry, I did not understand that instruction.'
	return statement(text).simple_card('GPIO Controller', text)

		


if __name__ == '__main__':
    app.run(debug=True)