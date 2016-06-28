# -*- coding: utf-8 -*-
"""
Created on Thu May 26 20:51:41 2016

@author: ysingh2
"""

import RPi.GPIO as gpio
import time
import json
from zeus import client as zc

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

z= zc.ZeusClient(<API_TOKEN>, 'api.ciscozeus.io')

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
	
while True:
    
    Dist= Dist_measure()
    PIR= PIR_measure()
    print int(Dist), PIR
#    print type(Dist), type(PIR)
    print (Dist>30 and PIR ==0), (Dist<0 and PIR ==0), (Dist<30 and PIR ==1), (Dist>30 and PIR ==1)

    if int(Dist)<30 and PIR ==1:
    	ts = time.time()
	print 'Case 1'
        # both on
	green1(0)
        yellow1(1)
        time.sleep(1)
        red1(1)
	yellow1(0)
	time.sleep(1)
        green2(1)
        red2(0)
        time.sleep(2)
	print Dist, PIR
	green2(0)
	yellow2(1)
	time.sleep(1)
	yellow2(0)
	green1(1)
        red1(0)
	red2(1)
	time.sleep(2)
    	
    	log= [{"timestamp":ts, "Street 1": 1, "Street 2": 1}]
    	z.sendLog("TrafficJunction", log)

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
	
    	log= [{"timestamp":ts, "Street 1": 1, "Street 2": 0}]
    	z.sendLog("TrafficJunction", log)

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

    	log= [{"timestamp":ts, "Street 1": 0, "Street 2": 1}]
    	z.sendLog("TrafficJunction", log)
    	
    elif int(Dist)>30 and PIR ==0:
    	ts = time.time()
	print 'Case 4'
        # 1 on 2 off, Assuming 1 is expected to have more vehicles than in 2.
	red1(0)
        green1(1)
        green2(0)
	yellow2(0)
	red2(1)             
	time.sleep(2)
 
    	log= [{"timestamp":ts, "Street 1": 0, "Street 2": 0}]
    	z.sendLog("TrafficJunction", log)
    	
gpio.cleanup()
'''url = 'http://127.0.0.1:8888/collect.PIR'+str(i)
r = requests.post(url, data = payload)
print('sent')'''
#converting metric to timestamp
#datetime.datetime.fromtimestamp(a[1][0]['points'][1][0]).strftime('%Y-%m-%d %H:%M:%S')
