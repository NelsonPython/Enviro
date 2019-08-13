# Publishing data to the I3 Data Marketplace

<b>This code walkthrough explains how to publish EnviroPhat data to the I3 Data Marketplace.</b>

### Checking prerequisites
Before you can publish data on the I3 Data Marketplace, use the [Connecting an IoT Device to the I3 Data Marketplace](https://github.com/NelsonPython/Connect_IoT_Device_to_I3).  It has step-by-step instructions for signing up at http://eclipse.usc.edu:8000 to get your API key and password and registering your product.

Decide how often you will publish data.  This script will publish data one time.  You can use cron to schedule it to publish data periodically, for example, every 30 minutes.  

### Importing libraries
```
#!/usr/bin/python

"""
Purpose: publish EnviroPhat environment data
"""
```
Import the [Eclipse Paho MQTT Python client library](https://pypi.org/project/paho-mqtt/) so you can publish sensor data to your subscribers 
```
import paho.mqtt.client as mqtt
```
In order for your data to be meaningful, you must report the time it was sensed so import time and datetime libraries

```
import time
import datetime
```
Data is passed using a json format so import json libraries
```
import json
```
Import the EnviroPhat libraries so you can take sensor readings
```
from envirophat import light, motion, weather,leds
```

### on_connect function

This function connects to the broker and prints the status of the connection
```
def on_connect(client, userdata, flags, rc):
    """printing out result code when connecting with the broker

    Args:
        client: publisher
        userdata:
        flags:
        rc: result code

    Returns:

    """

    m="Connected flags"+str(flags)+"\nresult code " +str(rc)+"\nclient1_id  "+st                                                                             r(client)
    print(m)
```
### on_message function

This function prints the sensor data
```
def on_message(client1, userdata, message):
    """printing out received message

    Args:
        client1: publisher
        userdata:
        message: recieved data

    Returns:

    """
    print("message received  "  ,str(message.payload.decode("utf-8")))
```

### getSensorData() function

This functions senses light, color, pressure, temperature, heading, accelerometer readings and provides device name, location and GPS coordinates of this device

```
def getSensorData():
    sensors = {}
    t = datetime.datetime.now()
    sensors["timestamp"] = str(t.strftime('%Y%m%d %H:%M'))
    sensors["device_name"] = "enviroPhat"
    sensors["city"] = 'Los Angeles'
    sensors["lng"] = '-118.323411'
    sensors["lat"] = '33.893916'

    sensors["lux"] = light.light()
    leds.on()
    sensors["rgb"] = str(light.rgb())[1:-1].replace(' ','')
    leds.off()
    sensors["accel"] = str(motion.accelerometer())[1:-1].replace(' ','')
    sensors["heading"] = motion.heading()
    sensors["temperature"] = weather.temperature()
    sensors["pressure"] = weather.pressure()

    return sensors
```
Use your account and password.  The topic is the product you are publishing on the I3 Data Marketplace.  The broker address and port are provided.

### main
```
if __name__ == '__main__':

    account = 'YourUsername'
    pw = 'YourPassword'
    topic = "Los Angeles Weather"

    try:
        pub_client = mqtt.Client(account)
        pub_client.on_connect = on_connect
        pub_client.on_message = on_message
        pub_client.username_pw_set(account, pw)
        pub_client.connect('18.217.227.236', 1883)      #connect to broker

    except Exception as e:
        print("Exception", str(e))

```
The payload contains the sensor data.  Once it is printed and published, the script disconnects.
```
    payload = getSensorData()
    print(payload)
    pub_client.publish(topic, json.dumps(payload))
    time.sleep(1)
    pub_client.disconnect()
```

### Example of sensor data being published

{'lux': 519, 'lat': '33.893916', 'city': 'Los Angeles', 'lng': '-118.323411', 'accel': '0.0732421875,-0.83001708984375,0.64324951171875', 'temperature': 33.86856647758932, 'pressure': 101279.19985577944, 'device_name': 'enviroPhat', 'timestamp': '20190812 19:06', 'rgb': '106,101,76', 'heading': 9.72, 'device_owner': 'Nelson@NelsonGlobalGeek.com'}