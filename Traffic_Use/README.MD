# Traffic Signal Application

In this use case, we create a traffic signal where two streets are merging which each other. The status of both the streets are continously uploaded to **Cisco-Zeus** cloud service. The following is the description of how the signals will behave. 

1. **No vehicles in both street**: If no vehicles are there in each Street, we will first calculate which street is busy by taking historical data from Cisco Zeus Cloud. If Street 1 is found to be busy, signal 1 will be green for and signal 2 will be red. Similarly if Street 2 is busier that Street 1, signal 2 will be green and signal 1 will be red. Only one signal is kept on to make sure that in any case no two signals at the same junction are green. Historical data of last 3 mins is queried from the cloud to make descison.

2. **Vehicle in Street1 & not in Street2**: In case vehicle is present in Street 1 and not in Street 2, the signal at Street 1 will turn red and Street 2 will be green as long as no vehicle is present in the other.

3. **Vehicle in Street2 & not in Street1**: Similar to case 2, when vehicle is in Street 2 and not in Street 1, Street 2 will have green and Street 1 will have red.

4. **Vehicles on both Streets**: When vehicles are present in both the Streets. We will again collect historical status of signal for last 3 mins. The signals will toggle from Street 1 to Street 2, but for twice the time in the busier street according to historical data. This will allow traffic to flow from both ends efficiently.

A schematic of the physical scenario is shown below.

<img src="https://raw.githubusercontent.com/yindolia/zeus-iot-1/master/Traffic_Use/Street%20Junction.png" >


###Hardware Used:

1. Raspberry Pi. (With WiFi connection via a dongle)
2. 2 Green, 2 Yellow and 2 Red LEDs for creating 2 traffic lights
3. A ultrasonic distance sensor
4. A motion (PIR) sensor
5. Accesories like Breadboard, Male-Male & Male-Female Jumper wires


<img src="https://raw.githubusercontent.com/yindolia/zeus-iot-1/master/Traffic_Use/Traffic-Signal-Setup-Hardware.jpg" >

###Architecture

Raspberry Pi collects data from Sensors which is uploaded to the cloud via zeus API (api.ciscozeus.io).

The data can be viewed and analysed over the cloud and can be used to send specific commands.

In present example the descison of which LED to light is done locally in the raspberry pi. This could be done on the cloud as complexity increases.

A schematic of the architecture is given below.

<img src="https://raw.githubusercontent.com/yindolia/zeus-iot-1/master/Traffic_Use/Architechture.png" >

###Program / Code
The program to run the application is written in Python, using the RPi.GPIO Library fro controling the GPIO pins of Raspberry Pi.

Two codes are prepared for the illustration.
`Traffic-Junction-RPi.py` in the repository only uploads data to Cisco Zeus Cloud, but do not rely on decison with historical data.
`Traffic-Junction-RPi-Ze
