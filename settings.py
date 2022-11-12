class Settings :
    def __init__(self):
        # store all of the settings 
        # ship settings 
        self.ship_speed = 1.5
        
        # bullet settings 
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (250,0,0) # red 
        self.bullets_allowed = 10

        # alien settings 
        self.alien_speed = 0.75
        self.fleet_drop_speed = 15 
        # fleet direction 1 for right -1 for left 
        self.fleet_direction = 1
        
        # screen settings 
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,0,50) # dark blue