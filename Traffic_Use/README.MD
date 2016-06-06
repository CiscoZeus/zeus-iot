# Traffic Signal Application

In this use case, we create a traffic signal where two streets are merging which each other. The following is the description of how it will work.

1. If no vehicles are there in each lane, Both the signals will remain green. This indicates that vehicles coming from any street will get indication to move.

2. In case vehicle is present in Street 1 and not in Street 2, the Signal at Street 2 will turn Red and Street 1 will stay red as long as no vehicle is present in the other.

3. Similarly, as in case 2, vice versa true for when vehicle in Street 2 and not in Street 1.

4. When vehicle is present in both the Streets. The signals will toggle from Street 1 to Street 2 every 5 seconds, allowing traffic to flow from both ends.


A schematic of the physical scenario is shown below.

<img src="https://raw.githubusercontent.com/yindolia/zeus-iot-1/master/Traffic_Use/Street%20Junction.png" >


###Hardware Used:

1. Raspberry Pi. (With WiFi connection via a dongle)
2. 2 Green, 2 Yellow and 2 Red LEDs for creating 2 traffic lights
3. A ultrasonic distance sensor
4. A motion (PIR) sensor
5. Accesories like Breadboard, Male-Male & Male-Female Jumper wires


<img src="https://raw.githubusercontent.com/yindolia/zeus-iot-1/master/Traffic_Use/Traffic-Signal-Setup.jpg" >
