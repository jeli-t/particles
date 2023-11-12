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


class Particle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PARTICLE_SIZE, PARTICLE_SIZE))
        self.image.fill(PARTICLE_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WINDOW_WIDTH)
        self.rect.y = random.randint(0, WINDOW_HEIGHT)


class Particle_system():
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Particle system")
        self.particles = pygame.sprite.Group()
        for _ in range(PARTICLE_QUANTITY):
            particle = Particle()
            self.particles.add(particle)
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

            self.render()
            pygame.time.Clock().tick(60)


if __name__ == "__main__":
    Particle_system()