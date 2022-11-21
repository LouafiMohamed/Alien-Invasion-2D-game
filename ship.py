import pygame 
from pygame.sprite import Sprite 

class Ship(Sprite):
    def __init__( self, ai_game,scale):
        # initialize the ship and set it's starting position 
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and set it's rect 
        self.image = pygame.image.load('imgs/ship2.bmp')
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.image = pygame.transform.scale(self.image , (int(self.width * scale),int(self.height * scale)))
        self.rect = self.image.get_rect()

        # start each new ship in the bottom center of the screen 
        self.rect.midbottom = self.screen_rect.midbottom

        # storing a decimal value for the horizontal position of the ship 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # movment flag 
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        # updating the ship position based on the movement flag 
        # updating the ship's value not the rect 
        if self.moving_right and self.rect.right < self.screen_rect.right + 60 :
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left> -60:
            self.x -= self.settings.ship_speed
        elif self.moving_up and self.rect.top > 0 :
            self.y -= self.settings.ship_speed
        elif self.moving_down  and self.rect.bottom < self.screen_rect.bottom :
            self.y += self.settings.ship_speed
        
        # update position 
        self.rect.x = self.x
        self.rect.y = self.y
    
    def center_ship(self):
        # center the ship on the screen 
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        # draw the ship at it's current position 
        self.screen.blit(self.image ,self.rect) 