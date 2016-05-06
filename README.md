#zeus-iot

##Raspberry Pi Integration with Zeus

### Hardware used

1. Raspberry Pi 2, Running a Raspbian (Debian jessie)
2. Ultrasonic distance Sensor. Model HC- SR04
3. PIR motion/presence sensor. 
4. Analog to Digital Converter(ADC), MCP3008 chip
5. Temperature Sensor, LM35
6. Luminosity Sensor, LDR

This tutorial consists of step by step guide to collect data of some standard sensors and upload them to Zeus cloud service for analysis.

I. Firstly open `Raspberry_Pi_Configuration.md` for getting started with Raspberry Pi. It will provide resources for installing all required components.

II. Next move to `Sensorsetup.md`. Here you will find details of all the above sensors and how to connect them to Raspberry Pi and log their dat.

III. Next step is to automatically upload the data to Zeus cloud. `DatauploadZeus.py`
