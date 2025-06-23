from pathlib import Path

class GameState():
    def __init__(self, game):
        self.settings = game.settings
        self.reset_game()
        self.high_score = self.settings.high_score
        self.level = self.settings.start_level
        self.get_saved_score()


    def reset_game(self):
        self.ships_left = self.settings.ship_life
        self.score = self.settings.start_game_score
        

    def get_saved_score(self):
        save_file = Path(self.settings.save_file)
        if save_file.exists():
            self.high_score = int(save_file.read_text())
    
    def save_saved_score(self):
        save_file = Path(self.settings.save_file)
        save_file.write_text(str(self.high_score))
        print('working dir', save_file.cwd())