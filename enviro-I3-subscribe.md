# Retrieving your data subscription

<b>This code walkthrough explains how to subscribe to EnviroPhat data published at the I3 Data Marketplace.</b>  EnviroPhat publishes environment data every 30 minutes.

## Setting up your subscription
Follow the [Connecting an IoT Device to the I3 Data Marketplace](https://github.com/NelsonPython/Connect_IoT_Device_to_I3) guide and subscribe to LA Weather Station (EnviroPhat)

## Subscribing to data
```
#!/usr/bin/python

"""
Purpose:  subscribing to EnviroPhat data from I3 Consortium Data Marketplace at http://eclipse.usc.edu:8000
"""
```

Import the [Eclipse Paho MQTT Python client library](https://pypi.org/project/paho-mqtt/) so you can subscribe to your data
```
import paho.mqtt.client as mqtt
```
In order for your data to be meaningful, you must report the time it was sensed.  Import time and datetime libraries

```
import time
import datetime
```
Data is passed using a json format so import json libraries
```
import json
```
### On_connect function

This function connects to the broker and prints the status of the connection
```
def on_connect(client, userdata, flags, rc):
    """ reporting IoT device connection """

    try:
        m = "Connected flags " + str(flags) + "\nResult code " + str(rc) + "\nClient_id  " + str(client)
        print(m)
        print("\n")
    except e:
        print("Hmmm I couldn't report the IoT connection: ", e)
```
### On_message function

This function receives data and stores it in csv format in the enviro.csv file

```
def on_message(client, userdata, msg):
    """ receiving data"""
    try:
        sensors = msg.payload
        sensors = json.loads(sensors.decode('utf-8'))
    except e:
        print("Check the message: ",e)

    logfile = open("enviro.csv","")
    print(sensors["timestamp"], ",",\
          sensors["device_name"], ",",\
          sensors["device_owner"], ",",\
          sensors["city"], ",",\
          sensors["lng"], ",",\
          sensors["lat"], ",",\
          sensors["lux"], ",",\
          sensors["rgb"], ",",\
          sensors["accel"], ",",\
          sensors["heading"], ",",\
          sensors["temperature"], ",",\
          sensors["pressure"], file=logfile)
    logfile.close()

    print("\nTimestamp: ", sensors["timestamp"])
    print("Device: ", sensors["device_name"])
    print("Device owner email: ", sensors["device_owner"])
    print("Device location: ", sensors["city"], " at longitude: ", sensors["lng"], " and latitude: ", sensors["lat"])
    print("Light: ", sensors["lux"])
    print("RGB: ", sensors["rgb"])
    print("Accelerometer: ", sensors["accel"])
    print("Heading: ", sensors["heading"])
    print("Temperature: ", sensors["temperature"])
    print("Pressure: ", sensors["pressure"])

    return sensors
```

### test_sub() function
This is the main loop.  The broker address and port are provided.

```
def test_sub():
    '''
    Broker address: 18.217.227.236 
    (ec2-18-217-227-236.us-east-2.compute.amazonaws.com)
    Broker port: 1883
    '''
```
Enter the topic you subscribed to along with your account and password
```    
    topic = "LA Weather Station"
    account = 'YourAccount'
    pw = 'YourPassword'
```
Connect to the broker
```
    sub_client = mqtt.Client(account)
    sub_client.on_connect = on_connect
    sub_client.on_message = on_message
    sub_client.username_pw_set(account, pw)
    sub_client.connect('18.217.227.236', 1883, 60) #connect to broker
    sub_client.subscribe(topic)
```
This script will listen until it is interrupted.  
```
    rc = sub_client.loop_forever()
    time.sleep(1)
    print("Return code ", rc)
```
Test_sub is a loop.  It can be stopped using the keyboard interrupt, ```ctrl-c```.
```
if __name__ == '__main__':
    try:
        test_sub()
    except KeyboardInterrupt:
        rc = sub_client.loop_stop()
        print("\nI'm stopping now")
```

### Sample data subscription

![screen capture of data described below](images/subscriptionData.png)

```

Connected flags {'session present': 0}
Result code 0
Client_id  <paho.mqtt.client.Client object at 0xb6a218d0>

Timestamp:  20190812 19:06
Device:  EnviroPhat
Device owner email:  Nelson@NelsonGlobalGeek.com
Device location:  Los Angeles  at longitude:  -118.323411  and latitude:  33.893916
Light:  519
RGB:  106,101,76
Accelerometer:  0.0732421875,-0.83001708984375,0.64324951171875
Heading:  9.72
Temperature:  33.86856647758932
Pressure:  101279.19985577944

```