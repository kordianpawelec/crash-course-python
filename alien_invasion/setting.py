class Settings:
    def __init__(self):
        #--game--
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_bg = (150,150,150)
        self.tick_rate = 60
        self.while_loops_atempts = 1000

        #--ship--
        self.ship_speed = 5.8

        #--bullets--
        self.bullet_speed = 10
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_colour = (60,60,60)
        self.bullets_allowed = 5

        #--stars-sky--
        self.amout_of_stars = 3000

        #--alien--
        self.alien_speed = 1
        self.army_drop_speed = 10
        self.army_dir = 1

        #--falling-stars--
        self.falling_star_colour = (252,252,252)
        self.falling_star_speed = 20
        self.falling_star_height = 80
        self.falling_star_width = 3
        self.number_of_stars_on_screen = 30
