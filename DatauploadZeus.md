To upload data to cisco Zeus cloud service following are the two ways

1. Using the API and clients provided by us. The official documentation is present at 

http://api.ciscozeus.io

The python program for sending metrics/data is provided here

/programs/sendMetricAPI.py 

This program can be used as an import or could be embedded in your main program.

2. Using Fluentd which was installed previously on Raspberry Pi. 

It posts a JSON which is a key-value pair with key = "Json" and value = a json consisting of the sensor values in string format. This is posted over localhost(Raspberry Pi) & 8888 port i.e. http://127.0.0.1:8888 tagged with 'Raspi'. Hence, the data will be taken into the Logs pipeline of Zeus.

The code is trying to replicate the following cURL command

`curl --data 'json={"sensor1": 100, "sensor2": 25}' http://localhost:8888/Raspi`

Fluentd is installed and configured to listen port 8888 on localhost. Fluend then transfers the Json to the Zeus Cloud.

