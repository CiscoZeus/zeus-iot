import RPi.GPIO as gpio
import time
import json
from zeus import client as zc

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(3,gpio.OUT)
gpio.setup(11,gpio.IN)
#f= open('/programs/pir')
#tym = ''

z= zc.ZeusClient('f0069791', 'api.ciscozeus.io')

while True:
	
	i= gpio.input(11)
	tym=time.time()
	PIRm=[{"timestamp":tym, "point":{"value":i}}]
	z.sendMetric("PIR", PIRm)
	r=z.getMetric(metric_name="PIR", from_date=tym)
	v= r["points"][0][2]
	if v==0:
		print "No one",i
		gpio.output(3,0)
		time.sleep(1)

	elif v==1:
		print "Someone",i
		gpio.output(3,1)
		time.sleep(1)
