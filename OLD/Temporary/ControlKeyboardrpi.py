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

# Initialize Pygame
pygame.init()

# Set up the display (required by Pygame, even if we won't use it)
screen = pygame.display.set_mode((640, 480))

# Set up a clock to manage the frame rate
clock = pygame.time.Clock()

def stop():
    gpio.output(mr1,0)
    gpio.output(ml1,0)
    gpio.output(mr2,0)
    gpio.output(ml2,0)

def stepper(dirf):
    gpio.output(dir,dirf)
    gpio.output(step,1)
    time.sleep(0.000015)
    gpio.output(step,0)
    time.sleep(0.000015)


def thd():
    global status
    while(status != -2):
        if(status>-1): stepper(status)

thf = threading.Thread(target=thd)
thf.start()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = -2
            gpio.cleanup()
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and event.key == pygame.K_a:
                print('turn left forward')
            elif event.key == pygame.K_s and event.key == pygame.K_a:
                print('turn left backward')
            elif event.key == pygame.K_a and event.key == pygame.K_s:
                print('turn right backward')
            elif event.key == pygame.K_d and event.key == pygame.K_s:
                print('turn right forward')
            elif event.key == pygame.K_w:
                stop()
                gpio.output(mr1,1)
                gpio.output(ml1,1)
                
                print('forward')
            elif event.key == pygame.K_s:
                gpio.output([ml2,mr2],1)
                gpio.output([ml1,mr1],0)
                print('backward')
            elif event.key == pygame.K_a:
                gpio.output([ml2,mr1],1)
                gpio.output([ml1,mr2],0)
                print('yawnleft')
            elif event.key == pygame.K_d:
                gpio.output([ml2,mr1],0)
                gpio.output([ml1,mr2],1)
                print('yawnright')
            elif event.key == pygame.K_c:
                gpio.output(pump,1)
                print('charge')
            elif event.key == pygame.K_SPACE:
                gpio.output(soli,1)
                print('shoot')
                time.sleep(0.5)
                gpio.output(soli,0)
            elif event.key == pygame.K_e:
                status = 1
            elif event.key == pygame.K_q:
                status = 0
        elif event.type == pygame.KEYUP:
            stop()
            status = -1
            gpio.output(pump,0)
            print('stop')


    clock.tick(60)
