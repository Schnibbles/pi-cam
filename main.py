from pijuice import PiJuice as pijuice
import time
import subprocess
import os
import requests
from datetime import datetime as dt

sleep = time.sleep

sleep(60)

os.system("sudo mount //192.168.1.131/film /media/pics/ -o password=")
os.system("sudo hwclock -w")
os.system("sudo shutdown 20:30")

number_of_pics = 0
pijuice = pijuice(1,0x14)
last_webhook_update = time.time() - 360
pijuice.rtcAlarm.SetWakeupEnabled(True)


now = dt.now()
foldername = now.strftime("%j")
command = "sudo mkdir /media/pics/images/" + foldername
os.system(command)

def digital_data():
  dict = pijuice.status.GetIoDigitalInput(2)
  status = dict["data"]
  return status


def photo(number_of_pics):
  global foldername
  filename = "/media/pics/images/" + foldername + "/image_" + str(number_of_pics) + ".jpg"
  subprocess.run(["sudo","raspistill","-t","2000","-o",filename])
  print("Taken a photo - current number of pics is ",number_of_pics)

def bird_check():
  if digital_data() == 1:
    sleep(1.5)
    if digital_data() == 1:
      global number_of_pics
      photo(number_of_pics)
      if number_of_pics < 300:
        number_of_pics = number_of_pics + 1
      else:
        number_of_pics = 0
    else:
      pass
  else:
    print("No motion","(",digital_data(),")")

def webhook_update():
  global last_webhook_update
  if time.time()-last_webhook_update >300:
    url = "http://192.168.1.131:8123/api/webhook/pi-cambatterypercentage"
    header = {
"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI2ODBiODZiNmQyYzc0MjY0OWVhZmMzMDVjNDExZTk2OCIsI>"}
    chargelevel = pijuice.status.GetChargeLevel()
    percentage = float(list(chargelevel.values())[0])
    chargelevel_percentage = {"data": percentage}
    ha = requests.post(url,json = chargelevel_percentage,headers = header)
    last_webhook_update = time.time()
    print("Successfully updated webhook")
  else:
    pass

while True:
  bird_check()
  webhook_update()
  sleep(1)
