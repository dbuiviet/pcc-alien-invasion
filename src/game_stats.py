class Game_Stats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        super().__init__()
        """Initialize statistics."""
        self.settings = ai_game.settings
        self._reset_stats()
        # Start Alien Invasion in an inactive state.
        self.game_active = False

    def _reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
