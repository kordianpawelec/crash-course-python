

class GameState():
    def __init__(self, game):
        self.settings = game.settings
        self.reset_game()

    def reset_game(self):
        self.ships_left = self.settings.ship_life
