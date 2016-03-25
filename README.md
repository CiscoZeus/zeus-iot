# zeus-iot

## Raspberry Pi integration with Cisco Zeus.

### Hardware used

1. Raspberry Pi 2, Running a Raspbian (Debian jessie variant)
2. Analog to Digital Converter(ADC), MCP3008 chip
3. Temperature Sensor LM35
4. Luminosity Sensor, LDR

![Photo of RPi Setup used](https://raw.githubusercontent.com/CiscoZeus/zeus-iot/master/Images/Rpi-Setup-Zeuss.jpg)

### Setup Instructions

1. Install Fluentd and plugins

    Raspbian has Ruby 1.9.3 bundled by default, but some more packages are required. In command prompt run following

  `sudo aptitude install ruby-dev`

  `sudo gem install fluend`

    Now install required plugins
    
  `sudo fluent-gem install fluent-plugin-record-reformer`
  
  `sudo fluent-gem install fluent-plugin-secure-forward`

2. Configuration file

    First to generate the Configuration file run following command.

  `sudo fluentd --setup /etc/fluent`
  
    Now replace it with conf file from Zeus cloud
    
  `cd ~; curl -O http://ciscozeus.io/td-agent.conf`
  
  `sudo cp td-agent.conf /etc/fluent/fluent.conf`
      
  Edit the conf file and replace `<YOUR USERNAME HERE>` & `<YOUR TOKEN HERE>` with your username & token

3. Run fluentd by command `sudo fluentd`

4. Run `Rpi-Temperature-Lux-zeus.py`

### Description

The sample program, `Rpi-Temperature-Lux-zeus.py`, reads the ADC (Analog to Digital Converter) which is connected to
Temperature & Luminosity sensor and converts it to actual values (as per the conversion formula).

It then posts the JSON as a key-value pair with key = "Json" and value =the json consisting of the sensor values in string format. 
This is posted over `localhost`(Raspberry Pi) & `8888` port i.e. `http://127.0.0.1:8888` tagged with `syslog.*`. 
Hence, the data will be taken into the Logs pipeline of Zeus.

The code is trying to replicate the following cURL command

`curl --data 'json={"sensor1": 100, "sensor2": 25}' http://localhost:8888/syslog.*`

Fluentd is installed and configured to listen port `8888` on `localhost`. Fluend then transfers the Json to the Zeus Cloud.
