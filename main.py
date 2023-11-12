import pygame
import sys

# Initialize Pygame
pygame.init()

# Config
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480


class Particle_system():
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Particle system")
        self.main_loop()

    def render(self):
        self.screen.fill((255, 255, 255))
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