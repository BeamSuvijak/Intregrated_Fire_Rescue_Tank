import keyboardPWM
import command
import time

print("booting... Please wait...")

while True:
    controlX = keyboardPWM.controlK
    command.update(controlX)
    
