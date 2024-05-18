import ControllingMethod

method = 0

"""
0 : Keyboard
1 : Joystick
2 : PID (auto)
"""

def readJoy(): ControllingMethod.Joystick.packaging()
def readKB(): ControllingMethod.KB.packaging()
def readPID(): ControllingMethod.PID.packaging()

usage = [readKB,readJoy,readPID]

controlling_value = usage[method]

if
