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
class MOTORPIN:
    def __init__(self,pwm,en1,en2):
        self.pwm = pwm
        self.en1 = en1
        self.en2 = en2
        gpio.setup(pwm,gpio.OUT)
        gpio.setup(en1,gpio.OUT)
        gpio.setup(en2,gpio.OUT)
        self.PWM = gpio.PWM(pwm,25000)
        self.PWM.start(0)
class MOTOR:
    def __init__(self,pwm,en1,en2):
        self.PIN = MOTORPIN(pwm,en1,en2)
        self.speed = 0
        self.dir = 0
    def execute(self):
        self.PIN.PWM.ChangeDutyCycle(abs(self.speed))
        if(dir):
            gpio.output(self.PIN.en1,1),gpio.output(self.PIN.en2,0)
        else: gpio.output(self.PIN.en1,0),gpio.output(self.PIN.en2,1)
    def update(self,dir,speed):
        self.speed = speed
        self.dir = dir
        self.execute()
steppin = 24
pindir = 22
pump = 26
soli = 29
liup = 21
lidown = 23
light = [8,10,12]

MOTORL = MOTOR(33,35,37)
MOTORR = MOTOR(32,36,38)

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
    if(logic<0): MOTORL.update(0,abs(logic))
    else: MOTORL.update(1,logic)

def driveR():
    logic = control["MOTOR"]["R"]
    if(logic<0): MOTORR.update(0,abs(logic))
    else: MOTORR.update(1,logic)


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
