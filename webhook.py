import http
import time
import requests
import json

from pijuice import PiJuice

pj = PiJuice(1,0x14)

chargelevel = pj.status.GetChargeLevel()
batterystatus = list(chargelevel.keys())[0]
print(batterystatus)

url = "http://192.168.1.131/api/webhook/pi-cambatterypercentage"
post = requests.post(url,batterystatus)

