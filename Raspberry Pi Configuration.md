#Raspberry Pi and Cisco Zeus

Raspberry Pi is one of the most common single board PC available which can run a full Linux distribution. This makes it identical for many IOT applications.
This guide will provide step by step instrution for configuring Raspberry Pi and connecting it to Cisco Zeus to upload sensor data.

##Step 1

Getting started with Raspberry Pi & Installing Raspbian

`https://www.raspberrypi.org/help/quick-start-guide/`

`https://www.andrewmunsell.com/blog/getting-started-raspberry-pi-install-raspbian/`

##Step 2 

Connecting to Wireless internet with Wi-Fi usb Dongle.

Open file /etc/network/interfaces and edit it as below


    auto lo

    iface lo inet loopback
    iface eth0 inet dhcp

    allow-hotplug wlan0
    auto wlan0

    iface wlan0 inet manual
    wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
`


Now open /etc/wpa_supplicant/wpa_supplicant.conf and add the following code to it

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

##Step 3

Installing the important components.

###a. Python

Python comes pre-loaded on Raspberry pi, but there are few more packages and libraries which would make programming Pi easier for us.
install the following libraries

*-RPi.GPIO*

`$ sudo apt-get install RPi.GPIO`

*-Zeus Python client,* 

`$ sudo pip install cisco-zeus`


###b. fluentd

**This is not needed if API is to be used**

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

Go to *`Sensorsetup.md`* for instruction on sensors available and can be used.


