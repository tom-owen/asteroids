import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface, color="white") -> None:
        pygame.draw.circle(surface=screen, color=color, center=self.position, radius=int(self.radius), width=LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt