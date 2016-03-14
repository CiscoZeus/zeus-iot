import spidev
import time
import requests
#import sys
#import collections
import json
spi = spidev.SpiDev()
spi.open(0, 0)

def readadc(adcnum):
# read SPI data from MCP3008 chip, 8 possible connections (0 thru 7)
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    #print r
    adcout = ((r[1] & 3) << 8) + r[2]
    return adcout

#timeSeries = {}
#readings = int(sys.argv[1])
#Convert recieved value to volts value. 3.3V is the supply given to ADC.
def VoltsConversion(data, places):
    volts = (data*3.3)/float(1023)
    volts = round(volts, places)
    return volts
#Converts temperature from volts to actual temperature.
def TempConversion(data, pos):
    temperature = ((data*330)/float(1023))-50
    temperature = round (temperature, pos)
    return temperature

host = "localhost"
port = 8888
    
while True:
    #Reading adc and conversion
    LuminosityLevel= readadc(0)
    LuminosityVal = VoltsConversion(LuminosityLevel,2)
    TemperatureLevel = readadc(2)
    TemperatureVolts = VoltsConversion(TemperatureLevel,2)
    TempVal= TempConversion (TemperatureVolts,2)
    #printing value
    print '_____________________________'
    print (TemperatureLevel, TemperatureVolts, TempVal)
    print (LuminosityLevel, LuminosityVal)
    time.sleep(3)
    
    #posts data over localhost at 8888
    newpayload={"json": json.dumps({"Temp":TempVal,
                                    "Lux":LuminosityVal})}
    url='http://127.0.0.1:8888/syslog.success'
    r= requests.post(url, data= newpayload)
    print('sent successfully')
    




