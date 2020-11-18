import math
import random
import pygame

from pygame import mixer
from api_test import current_moonphase


def main();
    # initialize
    pygame.init()
    sprites.initialize()

    # create the screen
    screen = pygame.display.set_mode((800, 600))

    # Load in the background
    background = pygame.image.load('images/background.png')

    # make caption for the window and add an icon
    pygame.display.set_caption("Hicks Space Invaders")
    icon = pygame.image.load('images/moon.png')
    pygame.display.set_icon(icon)

    # load the moon

    # load the enemies

    # load the ship

    # wait until the user closes the game



class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.x = 380
        self.y = 520
        self.x_change = 0

class Enemy(pygame.sprite.Sprite)
    def __init__(self):
        super().__init__()
        for i in range(num_enemies):
            #append enemy to list of enemies
            if i % 4 == 0:
                self.image = pygame.image.load('images/enemy.png')
                self.rect = self.image.get_rect()
            elif i % 4 == 1:
                self.image = pygame.image.load('images/enemy1.png')
                self.rect = self.image.get_rect()
            elif i % 4 == 2:
                self.image = pygame.image.load('images/enemy2.png')
                self.rect = self.image.get_rect()
            else:
                self.image = pygame.image.load('images/enemy3.png')
                self.rect = self.image.get_rect()
        self.x = []
        self.y = []
        self.x_change = []
        self.y_change = []
        self.count = 12


class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/laser.png')
        self.rect = self.image.get_rect()

class Moon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        if current_moonphase == 'New Moon':
            self.image = pygame.image.load('images/newmoon.png')

        if current_moonphase == 'Waxing Crescent':
            self.image = pygame.image.load('images/waxingcrescent.png')

        if current_moonphase == 'First Quarter':
            self.image = pygame.image.load('images/firstquarter.png')

        if current_moonphase == 'Waxing Gibbous':
            self.image = pygame.image.load('images/waxinggibbous.png')

        if current_moonphase == 'Full Moon':
            self.image = pygame.image.load('images/fullmoon.png')

        if current_moonphase == 'Waning Gibbous':
            self.image = pygame.image.load('images/waninggibbous.png')

        if current_moonphase == 'Last Quarter':
            self.image = pygame.image.load('images/lastquarter.png')

        if current_moonphase == 'Waning Crescent':
            self.image = pygame.image.load('images/waningcrescent.png')

        self.rect = self.image.get_rect()
        self.x = 660
        self.y = 35
        self.x_change = 0

def draw_enemys():
    #for loop to draw all enemies in the list from Enemy class


if __name__ == "__main__":
        main()