from pijuice import PiJuice as pijuice
from time import sleep
import subprocess
import os

os.system("sudo mount //192.168.1.131/film /media/pics/")

number_of_pics = 0
pijuice = pijuice(1,0x14)

def digital_data():
  dict = pijuice.status.GetIoDigitalInput(2)
  status = dict["data"]
  return status


def photo(number_of_pics):
  filename = "/media/pics/images/image_" + str(number_of_pics) + ".jpg"
  subprocess.run(["raspistill","-o",filename])
  print("Taken a photo - current number of pics is ",number_of_pics)

def bird_check():
  if digital_data() == 1:
    global number_of_pics
    photo(number_of_pics)
    number_of_pics = number_of_pics + 1
    sleep(2)
  else:
    sleep(1)
    print("No motion","(",digital_data(),")")

while True:
  bird_check()
  sleep(0.5)
