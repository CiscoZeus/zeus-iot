#This is an example of sensing and actuation. 
#We will make a LED glow when the PIR sensor detects motion.

import RPi.GPIO as gpio
import time
import json
import requests

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(3,gpio.OUT)
gpio.setup(11,gpio.IN)



while True:
	
	i= gpio.input(11)
	if i==0:
		print "No one",i
		gpio.output(3,0)
		time.sleep(1)
	#	payload= {"json": json.dumps({"PIR":"no one", "LED":"off"})}
		

	elif i==1:
		print "Someone",i
		gpio.output(3,1)
		time.sleep(1)
	#	payload= {"json": json.dumps({"PIR":"Someone", "LED":"on"})}
	
	'''url = 'http://127.0.0.1:8888/collect.PIR'+str(i)
	r = requests.post(url, data = payload)
	print('sent')'''

