import pygame


class Ship:
    """Class for manage the ship"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load image of the ship and get his rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # place each new ship in the center of the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # flag move
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update position of the ship in function flag 'moving_right' """
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
