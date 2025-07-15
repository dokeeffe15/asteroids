# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import *
from asteroidfield import *
from asteroids import *
import sys

def main():

    # initialize the pygame library
    pygame.init()

    print("Starting Asteroids!")
    print("Screen width:",SCREEN_WIDTH) 
    print("Screen height:",SCREEN_HEIGHT)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # delta time, the time since the last frame


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)



    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color="black", rect=None, special_flags=0)



        for x in drawable:
            x.draw(screen)
        updatable.update(dt)



        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                sys.exit()



        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
                    
         
            
            


        framerate = clock.tick(60) # It will pause the game loop until 1/60th of a second has passed.
        dt = framerate / 1000.0 # convert milliseconds to seconds   
        pygame.display.flip() #be sure to call this last in the loop



if __name__ == "__main__":
    main()