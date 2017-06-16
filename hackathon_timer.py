from flask import Flask, render_template
from flask_ask import Ask, statement
import random
import time
from threading import Thread



import json
from urllib import request



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
		data = '''{ "session": { "sessionId": "SessionId.a0af1b3c-5f93-4955-95d1-c8640446e290", "application": { "applicationId": "amzn1.ask.skill.305349ce-4e10-4ae7-94de-b7957590c8c2" }, "attributes": {}, "user": { "userId": "amzn1.ask.account.AEL2ZXVLXJJT7COFLTD52GCFVHRVLKD6ZGCH3EBN3AJUAIBQFFGNYDDDIUFF676LBLHDOGRHR7EJKLNV3GYHDFJFQDSJVIH4JNP44VSM5ICPB7MQTRKR46QPOYIPZT24MCUA32RH2542EVDOWD4BDZFZDYUPWLDJVI2XXB2XJTKE32VXUX234ILXDXNWWDSZQWCWF54EX4CQT5Q" }, "new": true }, "request": { "type": "IntentRequest", "requestId": "EdwRequestId.4a172517-3dc4-4b51-80d8-7a08bd4f1f5e", "locale": "en-GB", "timestamp": "2017-06-16T20:15:46Z", "intent": { "name": "Presenter", "slots": { "notification": { "name": "notification", "value": "1" }, "notification_units": { "name": "notification_units", "value": "minute" }, "timeout": { "name": "timeout", "value": "3" }, "timeout_units": { "name": "timeout_units", "value": "minutes" } } } }, "version": "1.0" }'''
		req = request.Request('http://localhost:5000')
		req.add_header('Content-Type', 'application/json')
		response = request.urlopen(req, data.encode())



if __name__ == '__main__':
    app.run(debug=True)