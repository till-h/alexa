from flask import Flask, render_template
from flask_ask import Ask, statement
import random
import time
from threading import Thread

app = Flask(__name__)
ask = Ask(app, '/')

@ask.intent('Presenter', convert={'timeout': int, 'notification': int})
def hackathon_timer(timeout, timeout_units, notification, notification_units):	
	text = render_template('hackathon_timer', timeout=timeout, timeout_units=timeout_units,
		notification=notification, notification_units=notification_units)
	timekeeper = timer()
	timekeeper.start()
	return statement(text).simple_card('Timekeeper', text)

class timer(Thread):
	def run(self):
		for i in range(1):
			time.sleep(10)
			print("iteration no: " + str(i))



if __name__ == '__main__':
    app.run(debug=True)