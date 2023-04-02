from pijuice import PiJuice as pijuice
import time

pijuice = pijuice(1,0x14)

while True:
  print(pijuice.status.GetIoDigitalInput(2)["data"])
  time.sleep(1)

