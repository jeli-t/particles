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
PARTICLE_SIZE = (4, 8)
PARTICLE_QUANTITY = 100
PARTICLE_SPEED = (2, 4)


class Particle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        size = (random.randint(*PARTICLE_SIZE))
        self.image = pygame.Surface((size, size))
        self.image.fill(PARTICLE_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WINDOW_WIDTH)
        self.rect.y = random.randint(0, WINDOW_HEIGHT)
        self.speed = (random.randint(*PARTICLE_SPEED))


    def update(self, direction):
        self.rect.x += direction.x * self.speed
        self.rect.y += direction.y * self.speed
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
        self.drawing_vector = False
        self.vector_start = Vector2(0, 0)
        self.vector_end = Vector2(0, 0)
        self.main_loop()


    def render(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.particles.draw(self.screen)
        if self.drawing_vector:
            pygame.draw.line(self.screen, (255, 0, 0), self.vector_start, self.vector_end, 3)
        pygame.display.flip()


    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.drawing_vector = True
                    x, y = pygame.mouse.get_pos()
                    self.vector_start = pygame.Vector2(x, y)
                    self.vector_end = pygame.Vector2(x, y)
                if event.type == pygame.MOUSEMOTION:
                    x, y = pygame.mouse.get_pos()
                    self.vector_end = pygame.Vector2(x, y)
                if event.type == pygame.MOUSEBUTTONUP:
                    direction_x = (self.vector_end[0] - self.vector_start[0]) / 40
                    direction_y = (self.vector_end[1] - self.vector_start[1]) / 40
                    self.direction = pygame.Vector2(direction_x, direction_y)
                    self.drawing_vector = False

            self.particles.update(self.direction)
            self.render()
            pygame.time.Clock().tick(60)


if __name__ == "__main__":
    Particle_system()