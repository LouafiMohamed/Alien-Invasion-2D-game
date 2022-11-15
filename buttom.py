import pygame.font 

class Buttom:
    def __init__(self,ai_game,msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # set a dimmention and proprieties of the buttom 
        self.width , self.height = 200 , 50 
        self.buttom_color = (60,100,150)
        self.text_color = (250,250,250)
        self.font = pygame.font.SysFont(None,48)

        # build the buttom's rect object and center it 
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        # the buttom msg needs to be prepped only once 
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        # turn the msg into a render img and center text on the buttom 
        self.msg_img = self.font.render(msg,True,self.text_color,self.buttom_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center 
    
    def draw_buttom(self):
        # draw blank buttom and then print out the text 
        self.screen.fill(self.buttom_color,self.rect)
        self.screen.blit(self.msg_img , self.msg_img_rect)