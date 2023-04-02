import requests
import json

url = "http://192.168.1.131:8123/api/webhook/pi-cambatterypercentage"

header = {
"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI2ODBiODZiNmQyYzc0MjY0OWVhZmMzMDVjNDExZTk2OCIsI>", "Content-Type": "application/json"}

chargelevel = {"data": float(35.4)}
print(chargelevel)
ha = requests.post(url,json = chargelevel,headers = header)
print(ha.status_code)