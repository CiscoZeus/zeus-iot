# -*- coding: utf-8 -*-
"""
Created on Thu May 26 20:51:41 2016

@author: ysingh2
"""

import RPi.GPIO as gpio
import time
import json
from zeus import client as zc
import datetime as dt


gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

z= zc.ZeusClient('f0069791', 'api.ciscozeus.io')

# Use BCM GPIO references
# instead of physical pin numbers


# Define GPIO to use on Pi
GPIO_TRIGGER = 13
GPIO_ECHO    = 16

# Set pins as output and input
gpio.setup(GPIO_TRIGGER,gpio.OUT)  # Trigger
gpio.setup(GPIO_ECHO,gpio.IN)      # Echo
gpio.setup(17,gpio.IN)    # PIR

 #LEDs
gpio.setup(4,gpio.OUT)
gpio.setup(5,gpio.OUT)
gpio.setup(6,gpio.OUT)
gpio.setup(12,gpio.OUT)
gpio.setup(23,gpio.OUT)
gpio.setup(24,gpio.OUT)

def red1(p):
	gpio.output(23, p)
	print 'red1',p
	
def red2(p):
	gpio.output(6, p)
	print p,'red2'

def green1(p):
	gpio.output(4, p)
	print p,'green1'

def green2(p):
	gpio.output(12, p)
	print p,'green2'

def yellow1(p):
	gpio.output(24, p)
	print p,'yellow1'

def yellow2(p):
	gpio.output(5, p)
	print p,'yellow2'


def Dist_measure():
    # Set trigger to False (Low)
    gpio.output(GPIO_TRIGGER, False)

    # Allow module to settle
    time.sleep(0.5)
    
    # Send 10us pulse to trigger
    gpio.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    gpio.output(GPIO_TRIGGER, False)
    start = time.time()
    
    while gpio.input(GPIO_ECHO)==0:
      start = time.time()
    
    while gpio.input(GPIO_ECHO)==1:
      stop = time.time()
    
    # Calculate pulse length
    elapsed = stop-start
    
    # Distance pulse travelled in that time is time
    # multiplied by the speed of sound (cm/s)
    distance = elapsed * 34300
    
    # That was the distance there and back so halve the value
    distance = distance / 2
    return distance

# Reset GPIO settings


def PIR_measure():
	
	i= gpio.input(17)
	return i
	#	payload= {"json": json.dumps({"PIR":"Someone", "LED":"on"})}


def getLastStatus():
	t = time.time()
	a = z.getLog("TrafficJunction", from_date = int (t-150), to_date = int(t), limit = 20)
	res = a[1]['result']
	sum1 =0
	sum2 = 1
	i =0
	for element in res:
		val1 = int(element['level'][0])
		val2 = int(element['level'][1])
		i = i+1
		sum1 = sum1+ val1
		sum2 = sum2+ val2
	if sum1>=sum2:
		return 1
	elif sum2>sum1:
		return 2


def signal1():
	green2(0)
	yellow2(1)
	time.sleep(1)
	yellow2(0)
	green1(1)
    red1(0)
	red2(1)
	time.sleep(2)
def signal2():
	green1(0)
    yellow1(1)
    time.sleep(1)
    red1(1)
	yellow1(0)
	time.sleep(1)
    green2(1)
    red2(0)
    time.sleep(2)


while True:
    
    Dist= Dist_measure()
    PIR= PIR_measure()
    print int(Dist), PIR
#    print type(Dist), type(PIR)
#    print (Dist>30 and PIR ==0), (Dist<0 and PIR ==0), (Dist<30 and PIR ==1), (Dist>30 and PIR ==1)
    latStat= getLastStatus()

		
    if int(Dist)<30 and PIR ==1:
		print 'Case 1', latStat
        # both on

		if latStat==1:
			signal1()
			signal1()
			signal2()
		elif latStat==2:
			signal2()
			signal2()
			signal1()	
	
	
		print Dist, PIR
	
		log = [{"level": "1 1"}]	
#		log = [{ "Street 1": 1, "Street 2":1}]
		z.sendLog("TrafficJunction", log)
		print log
		t= dt.datetime.fromtimestamp(int(ts)).strftime('%Y-%m-%d %H:%M:%S')
		print t

    elif int(Dist)>30 and PIR ==1:
		ts = time.time()
		print 'Case 2'
        # 1 on 2 off
		green1(1)
        yellow1(0)
		red1(0)
        green2(0)
		yellow2(0)
        red2(1)
		time.sleep(2)
		log = [{"level": "1 0"}]
#		log = [{ "Street 1": 1, "Street 2": 0}]
		z.sendLog("TrafficJunction", log)
		print log
		t= dt.datetime.fromtimestamp(int(ts)).strftime('%Y-%m-%d %H:%M:%S')

    elif int(Dist)<30 and PIR ==0:
		ts = time.time()
		print 'Case 3'
        # 1 on 2 off
		green1(0)
        yellow1(0)
        red1(1)
        green2(1)
        red2(0)
	
		time.sleep(2)
		log =[{"level":"0 1"}]
#		log = [{ "Street 1": 0, "Street 2":1}]
		z.sendLog("TrafficJunction", log)
		print log

    elif int(Dist)>30 and PIR ==0:
		if latStat==1:
			signal1()
		elif latStat ==2:
			signal2()
		print 'Case 4'
        # Toggle 1 and 2
	
		log = [{"level": "0 0"}]
#		log = [{ "Street 1": 0, "Street 2": 0}]
		z.sendLog("TrafficJunction", log)	
		print log
 
gpio.cleanup()
'''url = 'http://127.0.0.1:8888/collect.PIR'+str(i)
r = requests.post(url, data = payload)
print('sent')'''
#converting metric to timestamp
#datetime.datetime.fromtimestamp(a[1][0]['points'][1][0]).strftime('%Y-%m-%d %H:%M:%S')
