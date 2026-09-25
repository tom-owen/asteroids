import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.Surface, color="white") -> None:
        pygame.draw.circle(surface=screen, color=color, center=self.position, radius=int(self.radius), width=LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt