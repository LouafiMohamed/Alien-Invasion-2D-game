import pygame.font 
from pygame.sprite import Group 

from ship import Ship



class Scoreboard:
    def __init__(self,ai_game):
        """initialize the scorekeep attributes"""
        self.ai_game = ai_game 
        self.screen = ai_game.screen 
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings 
        self.stat = ai_game.stat 

        # Font settings for the scoring information 
        self.text_color = (100,170,200) # idk the color 
        self.font = pygame.font.SysFont(None,48)

        # prepare the initial score.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ship()

    def prep_score(self):
        # turn the score into a rendered image 
        rounded_score = round(self.stat.score , -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str , True,self.text_color,self.settings.bg_color)

        # display the score on the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20 
        self.score_rect.top =20 

    def show_score(self):
        # Draw the score and the high scoreon the screen 
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)


    def prep_high_score(self):
        # turn the high score into a rendered image 
        rounded_high_score = round(self.stat.high_score , -1)
        high_score_str = "High score: {:,}".format(rounded_high_score)
        self.high_score_image = self.font.render(high_score_str , True,self.text_color,self.settings.bg_color)

        # display the score on the top right of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = self.screen_rect.left + 20 
        self.high_score_rect.top =20 

    def check_high_score(self):
        if self.stat.score > self.stat.high_score:
            self.stat.high_score = self.stat.score
            self.prep_high_score()

    def prep_level(self):
        # turn the high score into a rendered image 
        level_str = "Level: {:,}".format(self.stat.level)
        self.level_image = self.font.render(level_str , True,self.text_color,self.settings.bg_color)

        # display the score on the top right of the screen.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.center = self.screen_rect.center 
        self.level_rect.top = 10 

    def prep_ship(self):
        # show how many ships are left 
        self.ships = Group()
        for ship_num in range(self.stat.ship_left):
            ship = Ship(self.ai_game,0.04)
            ship.rect.x = self.screen_rect.width -78 - ship_num*ship.rect.width   
            ship.rect.y = self.screen_rect.height -70
            # still didn't find a good place for those ships 
            self.ships.add(ship)
        
        