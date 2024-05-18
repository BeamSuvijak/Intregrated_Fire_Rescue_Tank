import pygame
import time
import sys
running = True
def setup():
    pygame.init()
    clock = pygame.time.Clock()

def read_KB():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check for key presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    print("x")
                if event.key == pygame.K_a:
                    print("x")
                if event.key == pygame.K_s:
                    print("x")
                if event.key == pygame.K_d:
                    print("x")
                if event.key == pygame.K_q:
                    print("x")
                if event.key == pygame.K_e:
                    print("x")
                if event.key == pygame.K_r:
                    print("x")
                if event.key == pygame.K_f:
                    print("x")
                if event.key == pygame.K_z:
                    print("x")
                if event.key == pygame.K_x:
                    print("x")
                if event.key == pygame.K_c:
                    print("x")
                if event.key == pygame.K_v:
                    print("x")
                if event.key == pygame.K_TAB:
                    print("x")
                if event.key == pygame.K_ESCAPE:
                    print("x")
                if event.key == pygame.K_LSHIFT:
                    print("x")
                if event.key == pygame.K_LCTRL:
                    print("x")

        time.sleep(0.01)

def quit():
    running = False
    time.sleep(1)
    pygame.quit()
    sys.exit()