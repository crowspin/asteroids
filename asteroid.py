import pygame, random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: return

        random_angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(random_angle)
        v2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        ast1 = Asteroid(self.position.x, self.position.y, new_radius)
        ast1.velocity = v1 * 1.2
        ast2 = Asteroid(self.position.x, self.position.y, new_radius)
        ast2.velocity = v2 * 1.2

