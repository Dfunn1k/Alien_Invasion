import sys
import pygame


class AlienInvasion:
    """Class to manage the resources and behaviors of game"""

    def __init__(self):
        """Initialize the game and create resource"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 675))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
            self.screen.fill(self.bg_color)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
