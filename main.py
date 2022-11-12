import sys
from time import sleep
import pygame

from aliens import Alien
from bullet import Bullet
from game_stats import GameStats 
from settings import Settings
from ship import Ship

#--------------------------------------------------------------

class AlienInvasion:
    # overall class to manage game assets and behavior 
    def __init__(self):
        # Initialize the game , and create the game resources 
        pygame.init()
        # all settings 
        self.settings = Settings()

        # size of normal screen 
        self.screen = pygame.display.set_mode((self.settings.screen_width ,self.settings.screen_height))
        
        pygame.display.set_caption("Alien Invasion") # the name that appere on top of the window 

        self.stat = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
    
    def _create_aliens(self, alien_num,row_num):
        #create an alien and place it in a row 
        alien = Alien(self)
        alien_width , alien_height = alien.rect.size
        alien.x = alien_width + 2*alien_width *alien_num
        alien.y = alien_height + 2*alien_height*row_num
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _create_fleet(self):
        # make an alien 
        alien = Alien(self)
        alien_width , alien_height = alien.rect.size
        avilibale_space_x = self.settings.screen_width   -  (2*alien_width) 
        avilibale_aliens_x = avilibale_space_x // (2 * alien_width )
        # determine how many rows are avilibles
        ship_height = self.ship.rect.height
        avilibale_space_y = self.settings.screen_height   - (3*alien_height) - ship_height  
        avilibale_rows = avilibale_space_y // (2*alien_height)

        # create the first row of aliens 
        for alien_num in range(avilibale_aliens_x):
            for row_num in range(avilibale_rows):
                self._create_aliens(alien_num,row_num)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event) 
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            


    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_UP:
            self.ship.moving_up = True

        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

        elif event.key == pygame.K_SPACE:
            self._fire_bullet() 

        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

        elif event.key == pygame.K_UP:
            self.ship.moving_up = False

        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False


    def _ship_hit(self):
        # responde when the ship get hit by an alien
        if self.stat.ship_left > 1:
            # decrement the ships left (life)
            self.stat.ship_left -= 1

            # get rid of remaning aliens and bullets 
            self.bullets.empty()
            self.aliens.empty()

            # create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # pause (sleep)
            sleep(0.5)
        else :
            self.stat.game_active = False


    def _fire_bullet(self):
        # create a bullet 
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _check_fleet_edges(self):
        # check if any alien touch the edge 
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break 
    
    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # treat this the same way when a ship got hit 
                self._ship_hit()
                break

        
    def _change_fleet_direction(self):
        # drop the whole fleet and change it's direction 
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
        

    def _update_aliens(self):
        # we have to check if the fleet is on the edge then we update.
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship ,self.aliens):
            self._ship_hit()
        
        # look for any ship that did hit the bottom 
        self._check_aliens_bottom()

        
    def _update_screen(self):
        # redraw background color 
        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()
        self.aliens.draw(self.screen)


        # drawing bullets 
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        
        # make the most resently drawn screen visible 
        pygame.display.flip()
    
    def _update_bullets(self):
        self.bullets.update()
            # getting rid  of bullet thta did disapear 
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets)) # just to check that it's really adding it to this group 
        self._check_alien_bullet_collisions()


    def _check_alien_bullet_collisions(self):
        # check if a bullet does hit a alien 
        # if so delete the bullet and the ship 
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        self._create_new_fleet_if_empty()

    def _create_new_fleet_if_empty(self):
        if not self.aliens:
            # destroy the existed bullets 
            self.bullets.empty()
            self._create_fleet()
    
        pass

    def run_game(self):
        # start the main loop for the game
        while True:
            self._check_events()
            if self.stat.game_active: 
                    # watch for keyboard and mouse input 
                    self.ship.update()
                    self._update_aliens()
                    self._update_bullets()
            self._update_screen()


        
if __name__ == '__main__':
    # make a game instance, and run the game 
    ai = AlienInvasion() # ai stand for alien invasion 
    ai.run_game()