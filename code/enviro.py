import time
import datetime
from envirophat import light, motion, weather,leds
from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import Tag
from iota import TryteString

def sendTX(msg):
    seed =    'YOURSEED9999999999999999999999999999999999999999999999999999999999999999999999999'
    address = 'ADDRESS9FROM9DIFFERENT9SEED999999999999999999999999999999999999999999999999999999999999999'
    #api = Iota('https://nodes.devnet.iota.org:443', seed)
    api = Iota('https://altnodes.devnet.iota.org', seed)
    tx = ProposedTransaction(
        address=Address(address),
        message=TryteString.from_unicode(msg),
        tag=Tag('ENVIROPHATDEMO'),
        value=0
    )
    try:
        tx = api.prepare_transfer(transfers=[tx])
    except Exception as e:
        print("Check prepare_transfer ", e)
        raise
    try:
        result=api.send_trytes(tx['trytes'],depth=3,min_weight_magnitude=9)
    except:
        print("Check send_trytes")

out=open('enviro.csv', 'a')

try:
        lux = light.light()
        leds.on()
        rgb = str(light.rgb())[1:-1].replace(' ','')
        leds.off()
        acc = str(motion.accelerometer())[1:-1].replace(' ','')
        heading = motion.heading()
        temp = weather.temperature()
        press = weather.pressure()
        timestamp = datetime.datetime.now()
        out.write('%f,%s,%s,%f,%f,%d,Los Angeles CA USA,' % (lux,rgb,acc,heading,temp,press))
        out.write(timestamp.strftime('%y-%m-%d %H:%M') +"\n")
        msg = str(lux)+","+str(rgb)+","+str(acc)+","+str(heading)+","+str(temp)+","+str(press)+",Los Angeles CA USA,"+str(timestamp)
        print(msg)
        sendTX(msg)

except Exception as e:
        print(e)

leds.off()
out.close()
