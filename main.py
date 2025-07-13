# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():

    # initialize the pygame library
    pygame.init()

    print("Starting Asteroids!")
    print("Screen width:",SCREEN_WIDTH) 
    print("Screen height:",SCREEN_HEIGHT)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color="black", rect=None, special_flags=0)
        pygame.display.flip() #be sure to call this last in the loop


if __name__ == "__main__":
    main()