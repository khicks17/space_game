import math
import random
import pygame

from pygame import mixer
from api_test import current_moonphase

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

class Enemy(pygame.sprite.Sprite)
    def __init__(self):
        super().__init__()
        self.image1 = pygame.image.load('images/enemy.png')
        self.rect1 = self.image1.get_rect()

        self.image2 = pygame.image.load('images/enemy1.png')
        self.rect1 = self.image2.get_rect()

        self.image3 = pygame.image.load('images/enemy2.png.png')
        self.rect1 = self.image3.get_rect()

        self.image4 = pygame.image.load('images/enemy3.png')
        self.rect1 = self.image4.get_rect()

class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/laser.png')
        self.rect = self.image.get_rect()

class Moon
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