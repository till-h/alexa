from flask import Flask, render_template
from flask_ask import Ask, statement
import random
import time
from threading import Thread
import webbrowser

app = Flask(__name__)
ask = Ask(app, '/')

@ask.intent('Presenter', convert={'timeout': int, 'notification': int})
def hackathon_timer(timeout, timeout_units, notification, notification_units):	
	text = render_template('hackathon_timer', timeout=timeout, timeout_units=timeout_units,
		notification=notification, notification_units=notification_units)
	timekeeper = timer()
	timekeeper.start()
	return statement(text).simple_card('Timekeeper', text)

@app.route('/start')
def start():
	return 'Starting...'

@app.route('/notification')
def notification():
	return 'Notification time!'

@app.route('/timeout')
def timeout():
	return render_template('youtube.html')

class timer(Thread):
	def run(self):
		webbrowser.open("http://localhost:5000/timeout")
		#webbrowser.open("http://localhost:5000/start", 1)
		time.sleep(5)
		webbrowser.open("http://localhost:5000/notification")
		time.sleep(5)
		webbrowser.open("http://localhost:5000/timeout")
		


if __name__ == '__main__':
    app.run(debug=True)