class Settings:
    def __init__(self):
        #--game--
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_bg = (150,150,150)
        self.tick_rate = 60
        self.while_loops_atempts = 1000
        self.start_game_score = 0
        self.score_image_offset = 20
        self.score_scale = 1.5
        self.high_score = 0
        self.save_file = 'save_file.cvs'
        self.start_level = 1

        #--ship--
        self.ship_life = 3

        #--bullets--
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (0,255,0)
        self.bullets_allowed = 5

        #--stars-sky--
        self.amout_of_stars = 3000

        #--alien--
        self.army_drop_speed = 10
        self.alien_points = 100
        self.bullet_colour_alien = (255,0,0)
        self.alien_bullet_speed = 5


        #--falling-stars--
        self.falling_star_colour = (252,252,252)
        self.falling_star_speed = 20
        self.falling_star_height = 80
        self.falling_star_width = 3
        self.number_of_stars_on_screen = 3

        #--button--
        self.button_width = 200
        self.buton_height = 50
        self.button_colour = (0,130,0)
        self.button_text_colour = (255,255,255)
        self.button_text_colour_score = (30,30,30)
        self.button_font_size = 48
        self.button_hover_colour = (0,255,0)

        #--game--
        self.speedup_scale = 1.1
        self.init_dynamic_settings()


    def init_dynamic_settings(self):
        self.ship_speed = 7
        self.bullet_speed = 10
        self.alien_speed = 4
        self.army_dir = 1

    
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        