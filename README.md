#Zeus-IOT

##Raspberry Pi Integration with Zeus

### Hardware used

1. Raspberry Pi 2, Running a Raspbian (Debian jessie)
2. Ultrasonic distance Sensor. Model HC- SR04
3. PIR motion/presence sensor. 
4. Analog to Digital Converter(ADC), MCP3008 chip
5. Temperature Sensor, LM35
6. Luminosity Sensor, LDR

##Usage

Raspberry Pi is one of the most common single board PC available which can run a full Linux distribution. This makes it identical for many IOT applications.
This guide will provide step by step instrution for configuring Raspberry Pi and connecting it to Cisco Zeus to upload sensor data.

###1. Getting started with Raspberry Pi

For installing OS & setting Raspberry Pi refer following links

`https://www.raspberrypi.org/help/quick-start-guide/`

`https://www.andrewmunsell.com/blog/getting-started-raspberry-pi-install-raspbian/`

###2. Connecting to Wireless internet with Wi-Fi usb Dongle.

Open file `/etc/network/interfaces` and edit it as below

    auto lo

    iface lo inet loopback
    iface eth0 inet dhcp

    allow-hotplug wlan0
    auto wlan0

    iface wlan0 inet manual
    wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
`

Now open `/etc/wpa_supplicant/wpa_supplicant.conf` and add the following code to it

    network= 
    {
    essid= <Your_WiFi_Name>
    psk = <Your_WiFi_password>
    key_mgmt= <Security_Type, WPA, WPA2, etc>
    }
  
If there are multiple WiFi hotspots, You can add each one as a seperate block in the same file.

Scan for available networks

`$ sudo iwlist wlan0 scan | grep essid`

Connect to the network once you see your network

`$ sudo iwconfig wlan0 essid <network_name>`

###3. Installing important components.

####a. Python

Python comes pre-loaded on Raspberry pi, but there are few more packages and libraries which would make programming Pi easier for us.
install the following libraries

*-RPi.GPIO*

`$ sudo apt-get install RPi.GPIO`

*-Zeus Python client,* 

`$ sudo pip install cisco-zeus`


####b. fluentd

**This is not needed if API is to be used for communication with Zeus Cloud**

Fluend is a daemon which is used to collect all data from all the sources and send it to the cloud is structured and secure way. It is done for data security and ease to handle multiple types and sources of data at the same time.

Raspbian distro comes with Ruby 1.9.3. We need some extra packages to install fluentd. Open terminal and run the following commands. (make sure internet is connected)

`$ sudo aptitude install ruby-dev`

`$ sudo gem install fluentd`

Now we need to install some more plugins for communicating with zeus

`$ sudo fluent-gem install fluent-plugin-record-reformer`

`$ sudo fluent-gem install fluent-plugin-secure-forward`

_Configuration file_

Firstly to generate the Configuration file run following command.

`$ sudo fluentd --setup /etc/fluent`

Now replace it with conf file from Zeus cloud

`$ cd ~; curl -O http://ciscozeus.io/td-agent.conf`

`$ sudo cp td-agent.conf /etc/fluent/fluent.conf`

Edit the conf file and replace <YOUR USERNAME HERE> & <YOUR TOKEN HERE> with your username & token

To run fluentd daemon run the following command

`$ sudo fluentd -c /etc/fluent/fluent.conf`

##Sensor Description & Usage

There are many sensors which can be used with Raspberry Pi. Below are some most common ones and the details on how to connect them.

###a. Ultrasonic sensor (Distance sensor)

These sensors transmit a sound signal and recieve the reflected signal. The time taken between these two events is recorded and is used for calculating the distance using `Distance= Time taken * Signal speed`

<img src="https://raw.githubusercontent.com/yindolia/zeus-iot-1/master/Images/HC-SR04-ultrasonic.jpg" width="500">

The following web-address provides detailed use of this sensor with Raspberry Pi.

http://www.raspberrypi-spy.co.uk/2012/12/ultrasonic-distance-measurement-using-python-part-1/

Also the python program used to collect data is included here.

`/programs/ultrasonic_Dist_Sensor.py`

###b. PIR (presence and motion) sensor

This sensor can be used to detect motion by any object or person which inturn is also indicative of presence or absence something moving. This can therefore be used to detect human presence. The connection of sensor. More details about the sensor are present in 

`http://www.instructables.com/id/PIR-Motion-Sensor-Tutorial/`

<img src="https://raw.githubusercontent.com/yindolia/zeus-iot-1/master/Images/PIR_sensor.jpg" width="500">

For using this sensor following python program has been included here.

`/programs/PIR_presence_sensor.py`

###c. Analog sensors

Analog sensors are sensors which produce voltage signal corresponding to the measured value. This includes, temperature (RTD, Thermocouple, Thermisters etc), Luminosity (LDR), Humidity, Accelerometers etc. These cannot be directly connected to Raspberry Pi as the Pi does not have any ADC on it. A external ADC like MCP3008 having 8 analog inputs has to be used for converting this into digtial Input which can be read by Raspberry Pi.


<img src="https://raw.githubusercontent.com/yindolia/zeus-iot-1/master/Images/mcp3008.jpg" width="200">

<img src="https://raw.githubusercontent.com/yindolia/zeus-iot-1/master/Images/analog-sensors.jpg" width="500">

For using these type of sensors, the program for measuring temperature & Luminosity has been included here. In reality this can be used with any type of analog sensor.

`/programs/Rpi-Analog-Sensors.py`

## Communicating with Zeus Cloud for analysis

To upload data to cisco Zeus cloud service, following are the two ways

####1. Using the API and clients provided by Zeus

The official documentation is present at 

`http://api.ciscozeus.io`

The python program for sending metrics/data is provided here

`/programs/sendMetricAPI.py`

This program can be used as an import or could be embedded in your main program.

####2. Using Fluentd 

Steps for installing Fluentd were provided at the beginning here while setting up Raspberry Pi. 

For feeding data to _fluentd_ a JSON which is a key-value pair with key = "Json" and value = a json consisting of the sensor values in string format. This is posted over localhost(Raspberry Pi) & 8888 port i.e. `http://127.0.0.1:8888` tagged with `'Raspi'`. Hence, the data will be taken into the Logs pipeline of Zeus.

The code is trying to replicate the following cURL command

`curl --data 'json={"sensor1": 100, "sensor2": 25}' http://localhost:8888/Raspi`

Fluentd is installed and configured to listen port 8888 on localhost. Fluend then transfers the Json to the Zeus Cloud.

##Sample Projects to try

These sensors can be used in multiple projects and IOT applications. Here are a few to try

1. __Motion sensing__

https://www.pubnub.com/blog/2015-06-16-building-a-raspberry-pi-motion-sensor-with-realtime-alerts/

2. __Plant water monitoring__

http://computers.tutsplus.com/tutorials/build-a-raspberry-pi-moisture-sensor-to-monitor-your-plants--mac-52875

3. __Sump/Tank Water level monitoring__

http://www.instructables.com/id/Sump-pump-water-level-The-hardware/


