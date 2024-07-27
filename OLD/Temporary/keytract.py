import pygame
import sys

esc = 41
W,A,S,D,C = 26,4,22,7,6
space = 44

def inn(lst:list,*args):
    args = set(args)
    return args.issubset(lst)

# def drive(control):
#     OUTPUT(L,control[0])
#     OUTPUT(R,control[1])

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
    if len(pressed_keys): print(pressed_keys )
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
    # print(motor)
    if((C in pressed_keys) and not (C in pre_pressed_keys)):
        charge = not charge
        # OUTPUT(pin,charge)charge
    print(inn(pressed_keys,space))
    for event in pygame.event.get(): continue


# Quit Pygame
pygame.quit()
sys.exit()