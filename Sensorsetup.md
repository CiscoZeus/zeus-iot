
There are many sensors which can be used with Raspberry Pi. Below are some most common ones and the details on how to connect them.


###1. Ultrasonic sensor (Distance sensor)

These sensors transmit a sound signal and recieve the reflected signal. The time taken between these two events is recorded and is used for calculating the distance using `Distance= Time taken * Signal speed`
/image/

The following web-address provides detailed use of this sensor with Raspberry Pi.

http://www.raspberrypi-spy.co.uk/2012/12/ultrasonic-distance-measurement-using-python-part-1/

Also the python program used to collect data is included here.

###2. PIR (presence and motion) sensor

This sensor can be used to detect motion by any object or person. This can therefore be used to detect human presence. The connection of sensor. More details about the sensor are present in 

`http://www.instructables.com/id/PIR-Motion-Sensor-Tutorial/`

/Image/

For using this sensor following python program has been included here.

PIR_presence_sensor.py

###3. Analog sensors

Analog sensors are sensors which produce voltage signal corresponding to the measured value. This includes, temperature (RTD, Thermocouple, Thermisters etc), Luminosity (LDR), Humidity, Accelerometers etc. These cannot be directly connected to Raspberry Pi as the Pi does not have any ADC on it. A external ADC like MCP3008 having 8 analog inputs has to be used for converting this into digtial Input which can be read by Raspberry Pi.

/Images/

For using these type of sensors, the program for measuring temperature & Luminosity has been included here. In reality this can be used with any type of analog sensor.

Rpi-Analog-Sensors.py

