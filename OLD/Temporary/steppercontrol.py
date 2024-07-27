import pygame
import sys
import time
import RPi.GPIO as gpio
import threading


status = -1
gpio.setmode(gpio.BOARD)

step = 40
dir = 38
liup = 33
lidown = 35
gpio.setup(step,gpio.OUT)
gpio.setup(dir,gpio.OUT)
gpio.setup(liup,gpio.IN)
gpio.setup(lidown,gpio.IN)

# Initialize Pygame
pygame.init()

# Set up the display (required by Pygame, even if we won't use it)
screen = pygame.display.set_mode((640, 480))

# Set up a clock to manage the frame rate
clock = pygame.time.Clock()


def stepper(dirf):
    gpio.output(dir,dirf)
    gpio.output(step,1)
    time.sleep(0.00015)
    gpio.output(step,0)
    time.sleep(0.00015)


def thd():
    global status
    while(True):
        if(status>-1): stepper(status)

thf = threading.Thread(target=thd)
thf.start()


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gpio.cleanup()
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_e:
                status = 1
            elif event.key == pygame.K_q:
                status = 0
        elif event.type == pygame.KEYUP: 
                status = -1
    clock.tick(60)
