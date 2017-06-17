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
	# convert times into seconds
	conversion_factor = { 'hour'   : 3600,
	                      'hours'  : 3600,
	                      'minute' : 60,
	                      'minutes': 60,
	                      'second' : 1,
	                      'seconds': 1}
	timeout = timeout * conversion_factor[timeout_units]
	notification = notification * conversion_factor[notification_units]
	presentation_timer = timer(timeout, notification)
	presentation_timer.start()
	return statement(text).simple_card('Presentation Timer', text)

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
	def __init__(self, timeout, notification):
		self.timeout = timeout
		self.notification = notification
	def run(self):
		webbrowser.open("http://localhost:5000/start")
		time.sleep(notification)
		webbrowser.open("http://localhost:5000/notification")
		time.sleep(timeout)
		webbrowser.open("http://localhost:5000/timeout")
		


if __name__ == '__main__':
    app.run(debug=True)