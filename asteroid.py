import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface, color="white") -> None:
        pygame.draw.circle(surface=screen, color=color, center=self.position, radius=int(self.radius), width=LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20,50)
        a1_vector = self.velocity.rotate(random_angle)
        a2_vector = self.velocity.rotate(-random_angle)
        smaller_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position[0], self.position[1], smaller_asteroid_radius)
        a2 = Asteroid(self.position[0], self.position[1] , smaller_asteroid_radius)
        a1.velocity = a1_vector * 1.2
        a2.velocity = a2_vector * 1.2

        