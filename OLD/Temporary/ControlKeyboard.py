import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display (required by Pygame, even if we won't use it)
screen = pygame.display.set_mode((640, 480))

# Set up a clock to manage the frame rate
clock = pygame.time.Clock()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.k_W and event.key == pygame.k_A:
                print('turn left forward')
            elif event.key == pygame.k_S and event.key == pygame.k_A:
                print('turn left backward')
            elif event.key == pygame.k_A and event.key == pygame.k_S:
                print('turn right backward')
            elif event.key == pygame.k_D and event.key == pygame.k_S:
                print('turn right forward')
            elif event.key == pygame.k_W:
                print('forward')
            elif event.key == pygame.k_S:
                print('backward')
            elif event.key == pygame.k_A:
                print('yawnleft')
            elif event.key == pygame.k_D:
                print('yawnright')


    clock.tick(60)
#