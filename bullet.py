import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):                                                       #Sprite is imported from pygame
    def __init__(self, ai_settings, screen, ship):                            #here we create a bullet object at the ship's current position
        super(Bullet, self).__init__()                                        #super is used to inherit properly from Sprite
        self.screen = screen

        #create a bullet rect at (0,0) and then set the current position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)  #this creates bullet's rect attribute
        self.rect.centerx = ship.rect.centerx       #we determine the bullet's centerx at the ship's centerx
        self.rect.top = ship.rect.top               #the bullet emerges from the top so it looks like it's getting fired

        #store the bullet's position as a decimal value
        self.y = float(self.rect.y)                 #make it a decimal to fine tune the bullet's speed

        self.color = ai_settings.bullet_color       #stores the bullet's color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        #move the bullet up the screen
        #update the decimal position of the bullet
        self.y -= self.speed_factor                 #subtract the amount stored in self.speed_factor from self.y
        #update the rect position
        self.rect.y = self.y                        #bullet position/speed updates

    def draw_bullet(self):
        #draw the bullet to the screen
        pygame.draw.rect(self.screen, self.color, self.rect)