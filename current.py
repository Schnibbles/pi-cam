import os
import time
from pijuice import PiJuice

pijuice = PiJuice(1,0x14)
while True:
   with open ('current.txt','a') as file:
     file.write(str(pijuice.status.GetIoCurrent()))
   print(str(pijuice.status.GetIoCurrent()))
   time.sleep(10)
