import pygame
import threading

control_template = {
    "MOTOR" : {
        "L" : 0, # range -100  <-> 100
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
controlK = control_template
esc = 41
W,A,S,D,C,Q,E = 26,4,22,7,6,20,8
Enter = 40
space = 44

def inn(lst:list,*args):
    args = set(args)
    # print(args.issubset(lst) )
    return args.issubset(lst)


def run(prn=False):
    global controlK
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pre_pressed_keys=[]
    pressed_keys = []
    running = True
    charge = False
    while running:
        precontrol = control_template
        keys = pygame.key.get_pressed()
        pre_pressed_keys = pre_pressed_keys
        pressed_keys = [k for k, v in enumerate(keys) if v]
        # print(pressed_keys)
        if esc in pressed_keys: running = False
        motor = [0,0]
        if(inn(pressed_keys,W,A)): motor = [100,0]
        elif(inn(pressed_keys,W,D)): motor = [0,100]
        elif(inn(pressed_keys,S,A)): motor = [-100,0]
        elif(inn(pressed_keys,S,D)): motor = [0,-100]
        elif(inn(pressed_keys,W)): motor = [100,100]
        elif(inn(pressed_keys,A)): motor = [100,-100]
        elif(inn(pressed_keys,S)): motor = [-100,-100]
        elif(inn(pressed_keys,D)): motor = [-100,100]
        precontrol["MOTOR"]["L"],precontrol["MOTOR"]["R"] = motor
        if(prn): print(motor[0],motor[1])

        if((space in pressed_keys) and not (space in pre_pressed_keys)):
            charge = not charge
            precontrol["pump"] = int(charge)
        precontrol["solinoid"] = int(inn(pressed_keys,Enter))

        for event in pygame.event.get(): continue

        if(inn(pressed_keys,Q)): status = 1
        elif(inn(pressed_keys,E)): status = 0
        else: status = -1

        precontrol["stepper"]["dir"] = abs(status)
        if status==-1: precontrol["stepper"]["operate"] = 0
        else: precontrol["stepper"]["operate"] = 1
        controlK = precontrol
    pygame.quit()

thd = threading.Thread(target=run)

if __name__  == "__main__":
    run(True)
else: thd.start()
