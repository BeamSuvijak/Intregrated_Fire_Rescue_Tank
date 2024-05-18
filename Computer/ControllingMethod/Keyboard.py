import pygame
import time
import sys
running = True
controlling = dict()
def setup():
    pygame.init()

def read_KB():
    global running, controlling
    running = True
    while running:
        pre_button_states = dict()
        L = 0
        R = 0
        Aiming = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check for key presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    L = 1
                    R = 1
                if event.key == pygame.K_a:
                    L = -1
                    R = 1
                if event.key == pygame.K_s:
                    L = -1
                    R = -1
                if event.key == pygame.K_d:
                    L = 1
                    R = -1
                if event.key == pygame.K_w and event.key == pygame.K_a:
                    L = 0
                    R = 1
                if event.key == pygame.K_w and event.key == pygame.K_d:
                    L = 1
                    R = 0
                if event.key == pygame.K_s and event.key == pygame.K_a:
                    L = 0
                    R = -1
                if event.key == pygame.K_s and event.key == pygame.K_d:
                    L = -1
                    R = 0
                if event.key == pygame.K_q:
                    Aiming = 1
                if event.key == pygame.K_e:
                    Aiming = -1
                if event.key == pygame.K_r:
                    pre_button_states["F7"] = 1
                if event.key == pygame.K_v:
                    pre_button_states["F9"] = 1
                if event.key == pygame.K_z:
                    pre_button_states["F0"] = 1
                if event.key == pygame.K_x:
                    print("x")
                if event.key == pygame.K_SPACE:
                    pre_button_states["F6"] = 1
                if event.key == pygame.K_RETURN:
                    pre_button_states["F4"] = 1
                    pre_button_states["F5"] = 1
                if event.key == pygame.K_TAB:
                    pre_button_states["F8"] = 1
                if event.key == pygame.K_ESCAPE:
                    pre_button_states["F10"] = 1
                    pre_button_states["F11"] = 1
                if event.key == pygame.K_LSHIFT:
                    print("x")
                if event.key == pygame.K_LCTRL:
                    print("x")
        button_states = pre_button_states
        controlling = {
            "Drive": {
                "L": {L},
                "R": {R}
            },
            "Aim" : Aiming ,
            "Button": button_states
        }
        time.sleep(0.01)

def quit():
    global running
    running = False
    time.sleep(1)
    pygame.quit()
    sys.exit()