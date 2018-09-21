import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):                #ship has access to the screen and settings
        # initialize the ship and its starting position
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings                      #variable to store the decimal values of speeds

        self.image = pygame.image.load('images/tank.png')   #Load the ship image and get its rect
        self.rect = self.image.get_rect()                   #gives the ship rectangle elements (hitbox?)
        self.screen_rect = screen.get_rect()                #position the ship at the bottom center

        self.rect.centerx = self.screen_rect.centerx        #position the center of the ship at the bottom center
        self.rect.bottom = self.screen_rect.bottom          #make the bottom of the ship and the rectangle's bottom the same

        self.center = float(self.rect.centerx)              #store a decimal value for the ship's center

        self.moving_right = False                           #right movement flag
        self.moving_left = False                            #left movement flag

    def update(self):                                       #update the ship's position based on the movement flag
        if self.moving_right and self.rect.right < self.screen_rect.right:  #if this value is less than the right end of the screen, keep going
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:         #same thing but for left bound
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center                     #update rect object from self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)             #draw the image

    def center_ship(self):
        #center the ship on the screen
        self.center = self.screen_rect.centerx