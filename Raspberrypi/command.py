import RPi.GPIO as gpio
import time
import threading

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
ml1,ml2,mr1,mr2 = 16,18,13,15
steppin = 40
pindir = 38
pump = 11
soli = 31
liup = 33
lidown = 35
light = [1,2,3]
"""
"""


def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(steppin,gpio.OUT)
    gpio.setup(pindir,gpio.OUT)
    gpio.setup(pump,gpio.OUT)
    gpio.setup(soli,gpio.OUT)
    gpio.setup(liup,gpio.IN)
    gpio.setup(lidown,gpio.IN)
    for pin in [16,18,13,15]: gpio.setup(pin,gpio.OUT)
init()

def driveL():
    logic = control["MOTOR"]["L"]
    if(logic==0): gpio.output([ml1,ml2],0)
    elif(logic==1): gpio.output(ml1,1),gpio.output(ml2,0)
    else: gpio.output(ml1,0),gpio.output(ml2,1)

def driveR():
    logic = control["MOTOR"]["R"]
    if(logic==0): gpio.output([mr1,mr2],0)
    elif(logic==1): gpio.output(mr1,1),gpio.output(mr2,0)
    else: gpio.output(mr1,0),gpio.output(mr2,1)

def stop():
    gpio.output(mr1,0)
    gpio.output(ml1,0)
    gpio.output(mr2,0)
    gpio.output(ml2,0)

def stepper():
    if(control["stepper"]["operate"]):
        gpio.output(pindir,control["stepper"]["dir"])
        gpio.output(steppin,1)
        time.sleep(0.00075)
        gpio.output(steppin,0)
        time.sleep(0.00075)

def relay():
    port = [11,31]
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
