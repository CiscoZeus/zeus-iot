# Traffic Signal Application

In this use case, we create a traffic signal where two streets are merging which each other. The following is the description of how it will work.

1. If no vehicles are there in each Street and assuming Street 1 is more busy than Street 2, signal at Street 1 will stay green and signal at street 2 will stay red. This is to make sure that in any case no two signals at the same junction are green.

2. In case vehicle is present in Street 2 and not in Street 1, the signal at Street 1 will turn red and Street 2 will be green as long as no vehicle is present in the other.

3. Similar to case 2, when vehicle is in Street 2 and not in Street 1, Street 2 will have green and Street 1 will have red.

4. When vehicle is present in both the Streets. The signals will toggle from Street 1 to Street 2 every 5 seconds, allowing traffic to flow from both ends.


A schematic of the physical scenario is shown below.

<img src="https://raw.githubusercontent.com/yindolia/zeus-iot-1/master/Traffic_Use/Street%20Junction.png" >


###Hardware Used:

1. Raspberry Pi. (With WiFi connection via a dongle)
2. 2 Green, 2 Yellow and 2 Red LEDs for creating 2 traffic lights
3. A ultrasonic distance sensor
4. A motion (PIR) sensor
5. Accesories like Breadboard, Male-Male & Male-Female Jumper wires


<img src="https://raw.githubusercontent.com/yindolia/zeus-iot-1/master/Traffic_Use/Traffic-Signal-Hardware.jpg" >

###Architecture

Raspberry Pi collects data from Sensors which is uploaded to the cloud via zeus API (api.ciscozeus.io).

The data can be viewed and analysed over the cloud and can be used to send specific commands.

In present example the descison of which LED to light is done locally in the raspberry pi. This could be done on the cloud as complexity increases.

A schematic of the architecture is given below.

<img src="https://raw.githubusercontent.com/yindolia/zeus-iot-1/master/Traffic_Use/Architechture.png" >

###Program / Code
The program to run the application is written in Python, using the RPi.GPIO Library fro controling the GPIO pins of Raspberry Pi.

Check `Traffic-Junction-RPi.py` in the repository.
