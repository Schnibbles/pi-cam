import os
import time
from pijuice import PiJuice

pijuice = PiJuice(1,0x14)
while True:
   with open ('battery.txt','a') as file:
     file.write(str(pijuice.status.GetChargeLevel()))
   print(str(pijuice.status.GetChargeLevel()))
   time.sleep(60)
