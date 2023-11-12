import pygame
import sys
import random
from pygame.math import Vector2

# Initialize Pygame
pygame.init()

# Config
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
BACKGROUND_COLOR = (0, 0, 0)
PARTICLE_COLOR = (255, 255, 255)
PARTICLE_SIZE = 4
PARTICLE_QUANTITY = 100
PARTICLE_SPEED = 2


class Particle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PARTICLE_SIZE, PARTICLE_SIZE))
        self.image.fill(PARTICLE_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WINDOW_WIDTH)
        self.rect.y = random.randint(0, WINDOW_HEIGHT)


    def update(self, direction):
        self.rect.x += direction.x * PARTICLE_SPEED
        self.rect.y += direction.y * PARTICLE_SPEED
        if self.rect.left > WINDOW_WIDTH:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = WINDOW_WIDTH
        if self.rect.top > WINDOW_HEIGHT:
            self.rect.bottom = 0
        elif self.rect.bottom < 0:
            self.rect.top = WINDOW_HEIGHT


class Particle_system():
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Particle system")
        self.particles = pygame.sprite.Group()
        for _ in range(PARTICLE_QUANTITY):
            particle = Particle()
            self.particles.add(particle)
        self.direction = pygame.Vector2(0, 1).rotate(random.uniform(0, 360))  # Initial random direction
        self.main_loop()


    def render(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.particles.draw(self.screen)
        pygame.display.flip()


    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.particles.update(self.direction)
            self.render()
            pygame.time.Clock().tick(60)


if __name__ == "__main__":
    Particle_system()