# Storing EnviroPhat data on the Tangle

<b>This code walkthrough explains how use the EnviroPhat environment sensor to sense data and store it on the Tangle.</b>

In order for sensor data to be meaningful, you must record the date and time the sensor reading was taken so import the time and datetime libraries.   

```
import time
import datetime
```
Import the EnviroPhat libraries so you can sense data
```
from envirophat import light, motion, weather,leds
```
Import the Iota libraries so you can send data to the Tangle
```
from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import Tag
from iota import TryteString
```

### sendTX() function
In order to send a transaction to the Tangle, you need two 81-tryte seeds.  The first seed is shown here.  It will send the transaction. Use python-iota-workshop/code/e04_generate_address.py to generate a second seed and attach an address.  Copy that address.  

```
def sendTX(msg):
        seed =    'FIRSTSEED999999999999999999999999999999999999999999999999999999999999999999999999'
        address = 'COPY9NEW9ADDRESS9FROM9SECOND9SEED9HERE9999999999999999999999999999999999999999999'
```
### Setting the testbed

For purposes of testing, connect to the IOTA testbed, called "Devnet"

```
        api = Iota('https://nodes.devnet.iota.org:443',seed)
```
### Sending the data transaction

To send a data transaction, you must format the address, message, tag, and value.  The address is the address that will receive the data.  The message contains the sensor data.  It must be converted to a TryteString.  The tag must be of type "Tag".  The value must be zero.

```
        tx = ProposedTransaction(
                address=Address(address),
                message=TryteString.from_unicode(msg),
                tag=Tag('ENVIROPHAT'),
                value=0
        )
```
There are two steps to sending a transaction:  preparing the transaction and sending the trytes.  In this example, an exception is raised if the transaction cannot be properly prepared.  However, an exception is not raised, if the transaction cannot be sent.

```
        try:
                tx=api.prepare_transfer(transfers=[tx])
        except Exception as e:
                print("Check prepare_transfer ", e)
                raise
        try:
                result=api.send_trytes(tx['trytes'],
                depth=3,min_weight_magnitude=9)
        except:
                print("Check send_trytes")
```
For testing purposes, a copy of data is stored in a CSV file.  Once you are confident in retrieving data from the Tangle, do not store data on the local device because the file becomes too large.

```
out=open('enviro.csv', 'a')
```
EnviroPhat reports the color near the sensor. 
```
try:
        lux = light.light()
```
In order to get a good view of the color, an LED onboard the sensor is turned on before the color reading it taken.  Then, it is turned off.
```
        leds.on()
        rgb = str(light.rgb())[1:-1].replace(' ','')
        leds.off()
```
Then the accelerometer, heading, temperature, and pressure readings are taken
```
        acc = str(motion.accelerometer())[1:-1].replace(' ','')
        heading = motion.heading()
        temp = weather.temperature()
        press = weather.pressure()
```
The timestamp is in Linux format which is difficult for humans to read.  Convert it to YYYY-MM-DD HH:MM format and write the sensor data to the test file.  
```
        timestamp = datetime.datetime.now()
        out.write('%f,%s,%s,%f,%f,%d,Los Angeles CA USA,' % (lux,rgb,acc,heading,temp,press))
        out.write(timestamp.strftime('%Y-%m-%d %H:%M') +"\n")
        msg = str(lux)+","+str(rgb)+","+str(acc)+","+str(heading)+","+str(temp)+","+str(press)+",Los Angeles CA USA,"+str(timestamp)
        print(msg)
```
Use the sendTX() function to send the data to the Tangle
```
        sendTX(msg)

except Exception as e:
        print(e)
```
Make sure the LED is off and close the test file
```
leds.off()
out.close()
```