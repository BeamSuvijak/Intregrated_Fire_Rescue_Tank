import pygame
import os
import time
import math
from threading import Thread

L = 0
R = 0
D = 0
deg=0
show = False
joystick = None
controlling = dict()
button_states = {}
aiming = 0


def ui(x,y):
    print(f"X : {x}")
    print(f"Y : {y}")
    print(f"D : {D}")
    print(f'Deg : {deg}')
    print(f"L : {L}")
    print(f"R : {R}")

    print("\n\n")

    for i in range(10,-10,-1):
        if(i==0):
            print("--------")
            continue
        if((L/10 >= i and i>0) or (L/10 <=i and i<0)): print("*",end='')
        else: print(" ",end='')
        print("       ",end='')
        if((R/10 >= i and i>0) or (R/10 <=i and i<0)): print("*")
        else: print(" ")


def mapping(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)

def calc(x,y):
    d = math.sqrt(x ** 2 + y ** 2)
    D = d
    deg = math.degrees(math.atan2(y, x))
    rev = deg < 0
    if (d > 100): d = 100
    if (not rev):
        l = 180 - deg
        r = deg
        if (l > 90): l = 90
        if (r > 90): r = 90
        l = mapping(l, 0, 90, 0, 100)
        r = mapping(r, 0, 90, 0, 100)

        L = l * d / 100
        R = r * d / 100
    else:
        r = deg
        l = -180 - deg
        L = mapping(l, -90, 0, -100, 0) * d / 100
        R = mapping(r, -90, 0, -100, 0) * d / 100
    return (L,R,D)

def packaging():
    global controlling
    controlling = {
        "Drive" : {
            "L" : L ,
            "R" : R
        },
        "Button" : button_states,
        "Aim" : aiming
    }
    return controlling


def run():
    global L, R, D, deg, button_states, aiming
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        x = math.ceil(joystick.get_axis(0) * 100)
        y = math.ceil(joystick.get_axis(1) * -100)
        L,R,D = calc(x,y)

        pre_button_states = {}
        for i in range(joystick.get_numbuttons()):
                pre_button_states[f'F{i}'] = joystick.get_button(i)
        button_states = pre_button_states
        aiming = joystick.get_hat(0)[1]
        time.sleep(0.01)
        # os.system('cls')
def setup():
    global show,joystick
    pygame.init()
    pygame.joystick.init()
    show = True
    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        print("No joystick found.")
    else:
        # Initialize the first joystick
        joystick = pygame.joystick.Joystick(0)
        joystick.init()

        print(f"Joystick Name: {joystick.get_name()}")
        print(f"Number of Axes: {joystick.get_numaxes()}")
        print(f"Number of Buttons: {joystick.get_numbuttons()}")


THREADrun = Thread(target=run)
