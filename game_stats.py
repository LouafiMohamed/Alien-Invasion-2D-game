

class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self._reset_stats()
        # start the game in a inactive state untill hut start buttom 
        self.game_active = False
        self.score = 0 
        self.high_score = 0 
        self.level = 1

    def _reset_stats(self):
        self.ship_left = self.settings.ship_limit