<h1>Saving Enviro data</h1>

You can post data to any popular data marketplace by sending it in csv or json format.  

<h3>CSV</h3>

csvEnviro.py will save sensor data in a csv file called enviro.csv in the following format.  You could add latitude, longitude, and device name

```
Light - enviro["lux"]
RGB red channel - enviro["red"]
RGB green channel - enviro["green"]
RGB blue channel - enviro["blue"]
Yaw - enviro["x"]
Pitch - enviro["y"]
Roll - enviro["z"]
Heading - enviro["heading"]
Temperature - enviro["temperature"]
Barometric pressure - enviro["pressure"]
Location
Timestamp
```

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
        enviro["red"] = rgb[0]
        enviro["green"] = rgb[1]
        enviro["blue"] = rgb[2]

        leds.off()

        print(enviro["lux"])
        print(enviro["red"])
        print(enviro["green"])
        print(enviro["blue"])


        acc = str(motion.accelerometer())[1:-1].replace(' ','')
        acc = acc.split(",")

        enviro["x"] = acc[0]
        enviro["y"] = acc[1]
        enviro["z"] = acc[2]

        enviro["heading"] = motion.heading()
        enviro["temperature"] = weather.temperature()
        enviro["pressure"] = weather.pressure()
        enviro["timestamp"] = datetime.datetime.now()

        enviro["lng"] = '-118.323411'
        enviro["lat"] = '33.893916'
        enviro["device_name"] = "Enviro"

        out.write('%f,%s,%s,%s,%s,%s,%s,%f,%f,%d,Los Angeles CA USA,' % \
                (enviro["lux"], \
                enviro["red"], \
                enviro["green"], \
                enviro["blue"], \
                enviro["x"], \
                enviro["y"], \
                enviro["z"], \
                enviro["heading"], \
                enviro["temperature"], \
                enviro["pressure"]))

        out.write(enviro["timestamp"].strftime('%y-%m-%d %H:%M') +"\n")

except Exception as e:
        print(e)

leds.off()
out.close()
```
