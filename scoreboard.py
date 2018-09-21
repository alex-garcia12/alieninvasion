import pygame.font
from ship import Ship
from pygame.sprite import Group

class Scoreboard():
    def __init__(self, ai_settings, screen, stats):
        #initialize scorekeeping attributes
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #font settings for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #prepare the initial score image
        self.prep_score()       #turns the text into an image
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()


    def prep_ships(self):
        #show how many ships are left
        self.ships = Group()            #holds ship instances
        for ship_number in range(self.stats.ships_left):    #loop runs for every ship the player has left
            ship = Ship(self.ai_settings, self.screen)      #create a new ship
            ship.rect.x = 10 + ship_number * ship.rect.width    #10 pix margin from the left
            ship.rect.y = 10    #10 pix margin from the top
            self.ships.add(ship)    #add the ships to the group


    def prep_score(self):
        #turn the score into a rendered image
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)       #turn score into a string (with rounding)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color) #creates the image

        #display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()       #rect for the scoreboard
        self.score_rect.right = self.screen_rect.right - 20 #right of the score rect is 20 pix away from edge of screen
        self.score_rect.top = 20    #20 pix down from top


    def prep_high_score(self):
        #turn the high score into a rendered image
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        #center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def prep_level(self):
        #turn the level into a rendered image
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

        #position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10


    def show_score(self):
        #draw score to the screen
        self.screen.blit(self.score_image, self.score_rect)     #draws the score image to the screen at the location specified by score_rect
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)