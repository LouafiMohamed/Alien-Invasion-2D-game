class Settings :
    def __init__(self):
        """Initialize the game's static settings"""
         
        # screen settings 
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,0,50) # dark blue

        # ship settings 
        self.ship_limit = 3
        
        
        # bullet settings 
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (250,0,0) # red 
        self.bullets_allowed = 10

        # alien settings 
        
        self.fleet_drop_speed = 15 
        
        # how quickly the game speed up 
        self.speedup_scale = 1.2

        # How quickly the alien point value increase 
        self.score_scale = 1.5
        # scoring 
        self.alien_points = 25
        
        self.initialize_dynamic_settings()



    def initialize_dynamic_settings(self):
        """initialize the settings that changes throught the game"""
        self.ship_speed = 1.5
        self.alien_speed = 1.0
        self.bullet_speed = 3.0

        # fleet direction 1 for right -1 for left 
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points) # just to check if it's increasing or not 
