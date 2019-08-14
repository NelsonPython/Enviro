#!/usr/bin/python

"""
Purpose: publishing EnviroPhat Weather Station data

"""
import paho.mqtt.client as mqtt
import time
import datetime
import json
from envirophat import light, motion, weather,leds

def on_connect(client, userdata, flags, rc):
    """printing out result code when connecting with the broker

    Args:
        client: publisher
        userdata:
        flags:
        rc: result code

    Returns:

    """

    m="Connected flags"+str(flags)+"\nresult code " +str(rc)+"\nclient1_id  "+str(client)
    print(m)



def on_message(client1, userdata, message):
    """printing out recieved message

    Args:
        client1: publisher
        userdata:
        message: recieved data

    Returns:

    """
    print("message received  "  ,str(message.payload.decode("utf-8")))

def getSensorData():
    sensors = {}
    t = datetime.datetime.now()
    sensors["timestamp"] = str(t.strftime('%Y%m%d %H:%M'))
    sensors["device_name"] = "YOUR DEVICE NAME"
    sensors["city"] = 'YOUR CITY'
    sensors["lng"] = 'YOUR LONGITUDE'
    sensors["lat"] = 'YOUR LATITUDE'

    sensors["lux"] = light.light()
    leds.on()
    sensors["rgb"] = str(light.rgb())[1:-1].replace(' ','')
    leds.off()
    sensors["accel"] = str(motion.accelerometer())[1:-1].replace(' ','')
    sensors["heading"] = motion.heading()
    sensors["temperature"] = weather.temperature()
    sensors["pressure"] = weather.pressure()

    return sensors

if __name__ == '__main__':

    account = 'YOUR-ACCOUNT'
    pw = 'YOUR-PASSWORD'
    topic = "YOUR ENVIROPHAT"

    try:
        pub_client = mqtt.Client(account)
        pub_client.on_connect = on_connect
        pub_client.on_message = on_message
        pub_client.username_pw_set(account, pw)
        pub_client.connect('18.217.227.236', 1883)      #connect to broker

    except Exception as e:
        print("Exception", str(e))

    payload = getSensorData()
    print(payload)
    pub_client.publish(topic, json.dumps(payload))
    time.sleep(1)
    pub_client.disconnect()
