import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Class to manage the resources and behaviors of game"""

    def __init__(self):
        """Initialize the game and create resource"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            # drawn the ship
            self.ship.blitme()
            # redraw the screen on each step throught the loop
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
