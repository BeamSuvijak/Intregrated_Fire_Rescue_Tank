import pygame
import sys
import time
import RPi.GPIO as gpio
import threading


gpio.setmode(gpio.BOARD)
status = -1
ml1,ml2,mr1,mr2 = 16,18,13,15
step = 40
dir = 38
pump = 11
soli = 31
liup = 33
lidown = 35
gpio.setup(step,gpio.OUT)
gpio.setup(dir,gpio.OUT)
gpio.setup(pump,gpio.OUT)
gpio.setup(soli,gpio.OUT)
gpio.setup(liup,gpio.IN)
gpio.setup(lidown,gpio.IN)
for pin in [16,18,13,15]: gpio.setup(pin,gpio.OUT)

esc = 41
W,A,S,D,C,Q,E = 26,4,22,7,6,20,8
space = 44

def inn(lst:list,*args):
    args = set(args)
    return args.issubset(lst)


def stop():
    gpio.output(mr1,0)
    gpio.output(ml1,0)
    gpio.output(mr2,0)
    gpio.output(ml2,0)

def stepper(dirf):
    gpio.output(dir,dirf)
    gpio.output(step,1)
    time.sleep(0.0015)
    gpio.output(step,0)
    time.sleep(0.0015)

def thd():
    global status
    while(status != -2):
        if(status>-1): stepper(status)
thf = threading.Thread(target=thd)
thf.start()

def driveL(control):
    if(control==0): gpio.output([ml1,ml2],0)
    elif(control==1): gpio.output(ml1,1),gpio.output(ml2,0)
    else: gpio.output(ml1,0),gpio.output(ml2,1)

def driveR(control):
    if(control==0): gpio.output([mr1,mr2],0)
    elif(control==1): gpio.output(mr1,1),gpio.output(mr2,0)
    else: gpio.output(mr1,0),gpio.output(mr2,1)

pygame.init()
screen = pygame.display.set_mode((640, 480))

pre_pressed_keys=[]
pressed_keys = []
running = True
charge = False
while running:
    keys = pygame.key.get_pressed()
    pre_pressed_keys = pre_pressed_keys
    pressed_keys = [k for k, v in enumerate(keys) if v]
    # print(pressed_keys)
    if esc in pressed_keys: running = False
    motor = [0,0]
    if(inn(pressed_keys,W,A)): motor = [0,1]
    elif(inn(pressed_keys,W,D)): motor = [1,0]
    elif(inn(pressed_keys,S,A)): motor = [0,-1]
    elif(inn(pressed_keys,S,D)): motor = [-1,0]
    elif(inn(pressed_keys,W)): motor = [1,1]
    elif(inn(pressed_keys,A)): motor = [-1,1]
    elif(inn(pressed_keys,S)): motor = [-1,-1]
    elif(inn(pressed_keys,D)): motor = [1,-1]
    print(motor)
    driveL(motor[0]),driveR(motor[1])


    if((C in pressed_keys) and not (C in pre_pressed_keys)):
        charge = not charge
        gpio.output(pump,charge)
    gpio.output(soli,keyboard2New.py)
    for event in pygame.event.get(): continue

    if(inn(pressed_keys,Q)): status = 1
    elif(inn(pressed_keys,E)): status = 0
    else: status = -1


# Quit Pygame
pygame.quit()
sys.exit()