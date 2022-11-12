import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self , ai_game):
        # initialize the alien ship 
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings 
        
        
        # load the aliens ship and set it's rect 
        self.image = pygame.image.load("imgs/aliens.bmp")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.image = pygame.transform.scale(self.image , (int(self.width * 0.06),int(self.height * 0.08)))
        self.rect = self.image.get_rect()

        # start each new alien near the top left of the screen.
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height
    
    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
    
    def check_edges(self):
        self.screen_rect = self.screen.get_rect()
        if self.rect.right >= self.screen_rect.right or self.rect.right <= 70:
            return True
            


    def blitme(self):
        # draw the aliens ship at it's current position 
        self.screen.blit(self.image ,self.rect)