from circleshape import *
from constants import *
from player import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        

    def draw(self, screen):
        pygame.draw.line(screen, "gray",(int(self.position.x), int(self.position.y)), (int(self.position.x) + SHOT_RADIUS, int(self.position.y) + SHOT_RADIUS), width=1) 


    def update(self, dt):
        self.position += self.velocity * dt

    def shoot(self):
        vector = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity += vector * PLAYER_SHOT_SPEED
       
 





   
 