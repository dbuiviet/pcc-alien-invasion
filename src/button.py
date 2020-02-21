import pygame.ftfont


class Button:
    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
