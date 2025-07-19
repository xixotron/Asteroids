import pygame
import random

from circleshape import CircleShape
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

        if self.position.x >= SCREEN_WIDTH + self.radius:
            self.position.x -= SCREEN_WIDTH + self.radius * 2
        elif self.position.x <= 0 - self.radius:
            self.position.x += SCREEN_WIDTH + self.radius * 2

        if self.position.y >= SCREEN_HEIGHT + self.radius:
            self.position.y -= SCREEN_HEIGHT + self.radius * 2
        elif self.position.y <= 0 - self.radius:
            self.position.y += SCREEN_HEIGHT + self.radius * 2

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_velocity = self.velocity * 1.2

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid1.velocity = new_velocity.rotate(random_angle)
        asteroid2.velocity = new_velocity.rotate(-random_angle)
        
