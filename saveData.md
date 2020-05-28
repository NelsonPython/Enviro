<h1>Sending sensor data in csv or json format</h1>

You can post data to any popular data marketplace by sending it in csv or json format.  For teaching purposes, csvEnviro.py will save sensor data in text format in a csv file called enviro.csv.  Saving data in text format and saving data onboard Enviro are not recommended for experiments that gather large quantities of data.  

<h3>csv</h3>

```
from envirophat import light, motion, weather,leds

import time
import datetime

out=open('enviro.csv', 'a')

enviro = {}
try:
        enviro["lux"] = light.light()
        leds.on()
        rgb = str(light.rgb())[1:-1].replace(' ','').split(",")
        enviro["RGB_red"] = rgb[0]
        enviro["RGB_green"] = rgb[1]
        enviro["RGB_blue"] = rgb[2]

        leds.off()

        acc = str(motion.accelerometer())[1:-1].replace(' ','')
        acc = acc.split(",")

        enviro["acc_x"] = acc[0]
        enviro["acc_y"] = acc[1]
        enviro["acc_z"] = acc[2]

        enviro["heading"] = motion.heading()
        enviro["temperature"] = weather.temperature()
        enviro["pressure"] = weather.pressure()

        ts =  datetime.datetime.now()
        enviro["timestamp"] = ts.strftime('%Y-%m-%d %H:%M')

        enviro["lng"] = '-118.323411'
        enviro["lat"] = '33.893916'
        enviro["device_name"] = "Enviro"

        out.write('%f,%s,%s,%s,%s,%s,%s,%f,%f,%d,Los Angeles CA USA,' % \
                (enviro["lux"], \
                enviro["RGB_red"], \
                enviro["RGB_green"], \
                enviro["RGB_blue"], \
                enviro["acc_x"], \
                enviro["acc_y"], \
                enviro["acc_z"], \
                enviro["heading"], \
                enviro["temperature"], \
                enviro["pressure"]))

        out.write(enviro["timestamp"] +"\n")

        #print sensor data in json format
        print(enviro)

except Exception as e:
        print(e)

leds.off()
out.close()
```

Sample enviro.csv

```
857.000000,134,115,108,-0.9300537109375,0.26171875,0.09246826171875,4.510000,35.928739,99440,Los Angeles CA USA,2020-05-28 11:17
857.000000,134,115,108,-0.93218994140625,0.26153564453125,0.1015625,5.440000,35.940641,99442,Los Angeles CA USA,2020-05-28 11:17
863.000000,134,115,109,-0.9354248046875,0.26141357421875,0.1005859375,7.240000,36.102568,99443,Los Angeles CA USA,2020-05-28 11:20
```
<h3>json</h3>

For teaching purposes, most AI Lab experiments send text data in json format.

```
{'device_name': 'Enviro', 
'lat': '33.893916', 
'lng': '-118.323411', 
'lux': 857, 
'RGB_red': '134', 
'RGB_green': '115', 
'RGB_blue': '108', 
'pressure': 99440.64663964233, 
'temperature': 35.92873890723813, 
'heading': 4.51, 
'acc_x': '-0.9300537109375'}
'acc_y': '0.26171875', 
'acc_z': '0.09246826171875', 
'timestamp': '2020-05-28 11:17'}
```
