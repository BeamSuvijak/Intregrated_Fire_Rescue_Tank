import RPi.GPIO as gpio
import time


control = {
    "MOTOR" : {
        "L" : 0, # range -1  - 1
        "R" : 0
    },
    "solinoid" : 0,
    "pump" : 0,
    "stepper" : {
        "operate" : 0,
        "dir" : 0,
        "Limitup" : 0,
        "Limitdw" : 0
    },
    "light" : {
        "error" : 0,
        "connected" : 0,
        "operating" : 0
    }
}

"""
GPIO PIN
"""

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

class MOTORPIN:
    def __init__(self,en1,en2):
        self.en1 = en1
        self.en2 = en2
        gpio.setup(en1,gpio.OUT)
        gpio.setup(en2,gpio.OUT)
class MOTOR:
    def __init__(self,en1,en2):
        self.PIN = MOTORPIN(en1,en2)
        self.dir = 0
    def execute(self):
        if(self.dir>0): gpio.output(self.PIN.en1,1),gpio.output(self.PIN.en2,0)
        elif(self.dir<0): gpio.output(self.PIN.en1,0),gpio.output(self.PIN.en2,1)
        else: gpio.output(self.PIN.en1,0),gpio.output(self.PIN.en2,0)
    def update(self,dir):
        self.dir = dir
        self.execute()
steppin = 22
pindir = 24
pump = 26
soli = 29
liup = 21
lidown = 23
light = [8,10,12]

MOTORL = MOTOR(37,35)
MOTORR = MOTOR(38,36)

"""
"""


def init():
    print("setting up command...")
    gpio.setup(steppin,gpio.OUT)
    gpio.setup(pindir,gpio.OUT)
    gpio.setup(pump,gpio.OUT)
    gpio.setup(soli,gpio.OUT)
    gpio.setup(liup,gpio.IN)
    gpio.setup(lidown,gpio.IN)

init()

def driveL():
    logic = control["MOTOR"]["L"]
    MOTORL.update(logic)

def driveR():
    logic = control["MOTOR"]["R"]
    MOTORR.update(logic)


def stepper():
    if(control["stepper"]["operate"]):
        gpio.output(pindir,control["stepper"]["dir"])
        gpio.output(steppin,1)
        time.sleep(0.00075)
        gpio.output(steppin,0)
        time.sleep(0.00075)

def relay():
    port = [pump,soli]
    complogic = [control["pump"],control["solinoid"]]
    for k,v in enumerate(port):
        gpio.output(v,complogic[k])

def process():
    """ DRIVE """
    driveL(),driveR()

    """ STEPPER """
    stepper()

    """ RELAY """
    relay()

def update(REC_CTRL : dict):
    global control
    control = REC_CTRL
    process()

if __name__ == "__main__" :
    print("MAIN")
