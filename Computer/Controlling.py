import ControllingMethod.Keyboard as KB
import ControllingMethod.Joystick as JS
method = 0
PID = False

"""
0 : Keyboard
1 : Joystick
"""

def readJoy():JS.packaging()
def readKB():KB.packaging()

# def readPID():CM.PID.packaging().get("Drive")

def setup():
    global method
    KB.setup()
    try:
        method = JS.setup()
        JS.THREADrun.start()
        method = 1
    except:
        KB.run()
    print("M: ",method)

usage = [readKB,readJoy]

def fetch():
    global PID
    controlling_value = JS.packaging()
    controlling_value["Header"] = 'Control'
    prvpid = False
    if(controlling_value["Button"].get("F9") and controlling_value["Button"].get("F9")!=prvpid): PID,prvpid = not PID,PID

    # if(PID):
        # controlling_value["Drive"] = readPID()

    return controlling_value

def packaging(): return 0
