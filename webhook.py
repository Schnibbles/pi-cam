import http
import time
import requests
import json

from pijuice import PiJuice

pj = PiJuice(1,0x14)
url = "http://192.168.1.131:8123/api/webhook/pi-cambatterypercentage"

header = {
"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI2ODBiODZiNmQyYzc0MjY0OWVhZmMzMDVjNDExZTk2OCIsI>"}

while True:
  chargelevel_percentage = float(list(pj.status.GetChargeLevel().values()[0]))
#  percentage = float(list(chargelevel.values())[0])
  chargelevel = {"data": chargelevel_percentage}
  ha = requests.post(url,json = chargelevel,headers = header)
  time.sleep(300)
  
