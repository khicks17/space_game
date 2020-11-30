import pygame
import

NUM_ENEMIES = 12
enemies = []
BLOCKSIZE = 100
SHIP_X_DELTA = 6

LASER_X = 0
LASER_Y = 480
LASER_STATE = "ready"
LASER_DELTA = 15

ENEMY_Y_DELTA = 40
ENEMY_X_DELTA = 4

MOON_X = 660
MOON_Y = 35

class Ship(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y


    def move_left(self):
        self.x = self.x - SHIP_X_DELTA

    def move_right(self):
        self.x = self.x + SHIP_X_DELTA

class Enemy(pygame.sprite.Sprite):
    def __init__(self,image_name,row,col):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.x = row * BLOCKSIZE
        self.y = col * BLOCKSIZE
        self.x_change = 0  # move along X
        self.y_change = 0  # move along Y

    def move_horizontal(self):
        self.x += ENEMY_X_DELTA

    def move_vertical(self):
        self.y += ENEMY_Y_DELTA

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
        self.x = MOON_X
        self.y = MOON_Y


    def displayMoon(self):
        screen.blit(self.image, self.x, self.y)

class Laser(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('images/laser.png')
        self.rect = self.image.get_rect()
        self.laser_state = "ready"
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 15

    def fire_laser(self,x,y):
        if self.laser_state is "ready":
            laserSound = mixer.Sound("sounds/laser.wav")
            laserSound.play()
            # Get the current x coordinate of the spaceship
            self.x = ship.x
            self.y = ship.y
