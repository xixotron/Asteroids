import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS, SHOT_DURATION

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.duration = SHOT_DURATION

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        if self.duration < 0:
            self.kill()
            return
        self.duration -= dt
        super().update(dt)
