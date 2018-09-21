import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from pygame.sprite import Group

def run_game():                                     #Here we initialize game and create a screen object
    pygame.init()                                   #this initializes background settings
    ai_settings = Settings()
    screen = pygame.display.set_mode\
    ((ai_settings.screen_width, ai_settings.screen_height)) #sets screen = settings attributes

    pygame.display.set_caption("Alien Invasion")    #sets the name of the window

    bg_color = (230, 230, 230)                      #sets the background color (r, g, b)

    play_button = Button(ai_settings, screen, "Play")   #make a play button
    ship = Ship(ai_settings, screen)                #make a ship
    alien = Alien(ai_settings, screen)              #make an alien
    bullets = Group()                               #group where bullets are stored
    aliens = Group()                                #group where aliens are stored
    stats = GameStats(ai_settings)                  #create an instance to store game statistics
    sb = Scoreboard(ai_settings, screen, stats)     #instance that scores game stats and create a scoreboard

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:                                     #loop that controls events while the game is running
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)     #checks for player input

        if stats.game_active:                                       #check if game is still active (still have ships left)
            ship.update()                                           #updates ship's position
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)  #updates bullets' positions
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)    #with updated positions of everything, draw new screens


run_game()