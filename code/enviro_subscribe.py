#!/usr/bin/python

"""
Purpose:  subscribing to enviroPhat Weather Station data from I3 Consortium Data Marketplace at http://eclipse.usc.edu:8000
"""

import paho.mqtt.client as mqtt
import time
import json
from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import Tag
from iota import TryteString
from json import load

def on_connect(client, userdata, flags, rc):
    """ reporting IoT device connection """

    try:
        m = "Connected flags " + str(flags) + "\nResult code " + str(rc) + "\nClient_id  " + str(client)
        print(m)
        print("\n")
    except e:
        print("Hmmm I couldn't report the IoT connection: ", e)

def on_message(client, userdata, msg):
    """ receiving data"""
    try:
        sensors = msg.payload
        sensors = json.loads(sensors.decode('utf-8'))
    except e:
        print("Check the message: ",e)

    logfile = open("enviro.csv", "a")
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


    api = Iota('https://nodes.devnet.iota.org:443') 
    address = 'H9TJVEEAOAI9ADCFSRIKOYHNLVDIRDIIREXQUJNBIWBSINJIJXXDTPTRDOZRRSCUOLZAXVZNRHDCWVSVD'
    tx = ProposedTransaction(
        address=Address(address),
        #message=TryteString.from_unicode(sensors),
        message=TryteString.from_unicode(json.dumps(sensors)),
        tag=Tag('ENVIROPHATIII'),
        value=0
    )
    print(tx)
    try:
        tx = api.prepare_transfer(transfers=[tx])
    except:
        print("PREPARE EXCEPTION",tx)
    try:
        result = api.send_trytes(tx['trytes'], depth=3, min_weight_magnitude=9)
    except:
        print("EXCEPTION", result)

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


def test_sub():
    '''
    Broker address: 18.217.227.236 (​ ec2-18-217-227-236.us-east-2.compute.amazonaws.com)
    Broker port: 1883
    account/pw:  username/password that you obtain from the marketplace
    topic: the name of the product that you purchased from the marketplace
    '''

    topic = "Los Angeles Weather"
    account = 'NelsonBuyor'
    pw = 'gxvjts'

    sub_client = mqtt.Client(account)
    sub_client.on_connect = on_connect
    sub_client.on_message = on_message
    sub_client.username_pw_set(account, pw)
    sub_client.connect('18.217.227.236', 1883, 60) #connect to broker
    sub_client.subscribe(topic)

    # get data while the return code is zero
    rc = 0
    while rc == 0:
        rc = sub_client.loop()
        time.sleep(1)
    print("Return code", rc)

if __name__ == '__main__':
    # subscribing to enviroPhat sensor data
    try:
        test_sub()
    except KeyboardInterrupt:
        logfile.close()
        print("\nI'm stopping now")
