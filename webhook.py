import http
import time
import requests

from pijuice import PiJuice

pj = PiJuice(1,0x14)

chargelevel = pj.status.GetChargeLevel()
batterystatus = list(chargelevel.values())[0]
print(batterystatus)

url = "192.168.1.131/api/webhook/pi-cambatterypercentage"
post = requests.post(url,batterystatus)

