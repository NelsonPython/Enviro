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
        enviro["timestamp"] = datetime.datetime.now()

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

        out.write(enviro["timestamp"].strftime('%y-%m-%d %H:%M') +"\n")

        #print sensor data in json format
        print(enviro)

except Exception as e:
        print(e)

leds.off()
out.close()
```

Sample enviro.csv

```
5154.000000,95,98,103,-0.53741455078125,0.821533203125,0.14166259765625,35.420000,38.998688,99049,Los Angeles CA USA,20-05-26 15:42
5260.000000,95,97,102,-0.54736328125,0.82244873046875,0.09747314453125,37.210000,39.151736,99051,Los Angeles CA USA,20-05-26 15:45
895.000000,138,109,100,-0.85943603515625,0.43939208984375,0.14556884765625,338.200000,35.846677,99044,Los Angeles CA USA,20-05-26 15:51
895.000000,138,110,100,-0.86138916015625,0.43853759765625,0.1348876953125,351.100000,38.174509,99041,Los Angeles CA USA,20-05-26 15:52
896.000000,138,110,101,-0.85516357421875,0.44140625,0.13079833984375,334.900000,38.465322,99041,Los Angeles CA USA,20-05-26 15:52
```
<h3>json</h3>

For teaching purposes, most AI Lab experiments send text data in json format.

```
{
'lat': '33.893916', 
'lng': '-118.323411', 
'lux': 835, 
'RGB_blue': '109', 
'RGB_green': '116', 
'RGB_red': '134', 
'temperature': 36.13952530025381, 
'heading': 0.45, 
'pressure': 99452.24100068159, 
'device_name': 'Enviro', 
'acc_x': '-0.9244384765625', 
'acc_z': '0.08563232421875', 
'acc_y': '0.25982666015625'
'timestamp': datetime.datetime(2020, 5, 28, 10, 53, 19, 614797), 
}
```

