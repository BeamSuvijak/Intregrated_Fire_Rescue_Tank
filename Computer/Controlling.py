import ControllingMethod

method = 0
PID = False

"""
0 : Keyboard
1 : Joystick
"""

def readJoy(): ControllingMethod.Joystick.packaging()
def readKB(): ControllingMethod.KB.packaging()

def readPID(): ControllingMethod.PID.packaging().get("Drive")

usage = [readKB,readJoy]
controlling_value = usage[method]

prvpid = False
if(controlling_value["F9"] and controlling_value["F9"]!=prvpid): PID,prvpid = not PID,PID

if(PID):
    controlling_value["Drive"] = readPID()
