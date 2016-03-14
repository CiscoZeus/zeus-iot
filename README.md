# zeus-iot

## Raspberry Pi integration with Cisco Zeus.

Hardware used

1. Raspberry Pi 2, Running a Raspbian (Debian jessie variant)
2. Analog to Digital Converter(ADC), MCP3008 chip
3. Temperature Sensor LM35
4. Luminosity Sensor, LDR

![Photo of RPi Setup used](https://raw.githubusercontent.com/yindolia/zeus-iot/master/Images/Rpi-Setup-Zeuss.jpg?token=AGL3osNIHEYvhsTXz_rtGci8Ssphbp8bks5W79JqwA%3D%3D)

The sample program, Rpi-Temperature-Lux-zeus.py, reads the ADC which is connected to Temperature & Luminosity sensor and converts it to actual values(as per the conversion formula).

It then posts the Json as a key value pair with key = "Json" and value as the json consisting of the sensor values. This is posted over localhost(Raspberry Pi) & 8888 port i.e. "http://127.0.0.1:8888" tagged with syslog.*. Hence, the data will be taken into the Logs pipeline of Zeus.

The code is trying to replicate the following cURL command

curl --data 'json={"sensor1": 100, "sensor2": 25}' http://localhost:8888/syslog.*

Fluentd is installed and configured to listen port 8888 on localhost. Fluend then transfers the Json to the Zeus Cloud.
