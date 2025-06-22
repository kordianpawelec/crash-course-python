class Settings:
    def __init__(self):
        #--game--
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_bg = (200,200,200)
        self.tick_rate = 60

        #--ship--
        self.ship_speed = 5.8

        #--bullets--
        self.bullet_speed = 10
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_colour = (60,60,60)
        self.bullets_allowed = 5

        #--stars-sky--
        self.amout_of_stars = 50