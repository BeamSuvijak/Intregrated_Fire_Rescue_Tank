import ControllingMethod as CM
method = 0
PID = False

"""
0 : Keyboard
1 : Joystick
"""

def readJoy():CM.Joystick.packaging()
def readKB():CM.KB.packaging()

def readPID():CM.PID.packaging().get("Drive")

def setup():
    global method
    CM.Keyboard.setup()
    try:
        CM.Joystick.setup()
        CM.Joystick.run()
        method = 1
    except:
        CM.Keyboard.run()

usage = [readKB,readJoy]

def fetch():
    controlling_value = usage[method]
    controlling_value["Header"] = "Control"

    prvpid = False
    if(controlling_value["F9"] and controlling_value["F9"]!=prvpid): PID,prvpid = not PID,PID

    if(PID):
        controlling_value["Drive"] = readPID()

    return controlling_value
