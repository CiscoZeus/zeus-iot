# zeus-iot

## Raspberry Pi integration with Cisco Zeus.

Hardware used

1. Raspberry Pi 2, Running a Raspbian (Debian jessie variant)
2. Analog to Digital Converter(ADC), MCP3008 chip
3. Temperature Sensor LM35
4. Luminosity Sensor, LDR

![Photo of RPi Setup used](https://raw.githubusercontent.com/yindolia/zeus-iot/master/Images/Rpi-Setup-Zeuss.jpg?token=AGL3osNIHEYvhsTXz_rtGci8Ssphbp8bks5W79JqwA%3D%3D)

Setup Instructions

1. Install Fluentd and plugins
    Raspbian has Ruby 1.9.3 bundled by default, but some more packages are required. In command prompt run following
  1.1 `sudo aptitude install ruby-dev`
  1.2 `sudo gem install fluend`
    Now install required plugins
  1.3 `sudo fluent-gem install fluent-plugin-record-reformer`
  1.4 `sudo fluent-gem install fluent-plugin-secure-forward`

2. Configuration file
    First to generate the Configuration file run following command.
  2.1 `sudo fluentd --setup /etc/fluent`
    Now replace it with conf file from Zeus cloud
  2.2 `cd ~; curl -O http://ciscozeus.io/td-agent.conf` 
      `sudo cp td-agent.conf /etc/fluent/fluent.conf`
  2.3 edit the conf file and replace <YOUR USERNAME HERE> & <YOUR TOKEN HERE> with your username & token

3. Run fluentd by command `sudo fluentd`

The sample program, `Rpi-Temperature-Lux-zeus.py`, reads the ADC which is connected to Temperature & Luminosity sensor and converts it to actual values(as per the conversion formula).

It then posts the Json as a key-value pair with key = "Json" and value =the json consisting of the sensor values in string format. This is posted over localhost(Raspberry Pi) & 8888 port i.e. "http://127.0.0.1:8888" tagged with syslog.*. Hence, the data will be taken into the Logs pipeline of Zeus.

The code is trying to replicate the following cURL command

`curl --data 'json={"sensor1": 100, "sensor2": 25}' http://localhost:8888/syslog.*`

Fluentd is installed and configured to listen port 8888 on localhost. Fluend then transfers the Json to the Zeus Cloud.
