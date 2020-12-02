import pygame


X_BLOCKSIZE = 100
X_OFFSET = 50
Y_BLOCKSIZE = 60
Y_OFFSET = 120

HEIGHT = 600
WIDTH = 800

SHIP_X_DELTA = 10

LASER_X = 0
LASER_Y = 480
LASER_STATE = "ready"
LASER_DELTA = 15

ENEMY_Y_DELTA = 40
ENEMY_X_DELTA = 4

MOON_X = 710
MOON_Y = 65

SHIP_X = 380
SHIP_Y = 520

class Ship(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.ship_speed = 0


    def move_left(self):
        self.ship_speed = -SHIP_X_DELTA

    def move_right(self):
        self.ship_speed = SHIP_X_DELTA

    def update(self, *args, **kwargs) -> None:
        self.rect.centerx += self.ship_speed

    def stop(self):
        self.ship_speed = 0

class Enemy(pygame.sprite.Sprite):
    def __init__(self,image_name,row,col, level):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.rect.centerx = (col*X_BLOCKSIZE) + (X_OFFSET)
        self.rect.centery = (row*Y_BLOCKSIZE) + (Y_OFFSET)

        # Change this to low or speed up how quickly the enemy speed increases
        self.x_speed = 4 + 2*level

    def update(self, *args, **kwargs) -> None:
        self.rect.centerx += self.x_speed


class Kill(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/kill.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.centery = 100

class Title(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/spaceinvaders_title.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 480
        self.rect.centery = 40


class Moon(pygame.sprite.Sprite):
    def __init__(self, current_moonphase):
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
        self.rect.centerx = MOON_X
        self.rect.centery = MOON_Y



class Laser(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('images/laser.png')
        self.rect = self.image.get_rect()
        self.laser_state = "ready"
        self.rect.centerx = x
        self.rect.centery = y
        self.laser_speed = 0

    def update(self, *args, **kwargs) -> None:
        self.rect.centery += self.laser_speed