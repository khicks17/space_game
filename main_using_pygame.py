# Portions of coded modified from the link below
# Sounds taken from github file
# https://github.com/attreyabhatt/Space-Invaders-Pygame

import random
import pygame
from pygame import mixer

from api_test import current_moonphase

NUM_ENEMIES = 12
enemies = []
BLOCKSIZE = 100
SHIP_XDELTA = 6

LASER_X = 0
LASER_Y = 480
LASER_STATE = "ready"
LASER_DELTA = 15

ENEMY_YDELTA = 40
ENEMY_XDELTA = 4

MOON_X = 660
MOON_Y = 35


pygame.init()
clock = pygame.time.Clock()
FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('images/background.png')

# Score
score_value = 0
font = pygame.font.Font('font/space_invaders.ttf', 22)
# game over
game_over_font = pygame.font.Font('font/space_invaders.ttf', 50)


def show_score():
    textX = 10
    textY = 10
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (textX, textY))

def game_over_text():
    game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over_text, (x, y))

def title(x, y):
    titleImg = pygame.image.load('images/spaceinvaders_title.png')
    screen.blit(titleImg, (x, y))

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.x = 380
        self.y = 520
    def showShip(self):
        screen.blit(self.image, self.x, self.y)

    def move_left(self):
        self.x = self.x - SHIP_XDELTA

    def move_right(self):
        self.x = self.x + SHIP_XDELTA


class Enemy(pygame.sprite.Sprite):
    def __init__(self,image_name,row,col):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.x = row * BLOCKSIZE
        self.y = col * BLOCKSIZE
        self.move_x = 0  # move along X
        self.move_y = 0  # move along Y
        self.count = 12

    def draw_enemies(self):
        for i in range(NUM_ENEMIES):
            image_name = "images/enemy%d.png" % (i % 4)
            row = ((i % 6) + 20)
            col = i
            enemies.append(Enemy(image_name, row, col))
        screen.blit(enemies, self.x, self.y)

    def move_horizontal(self):
        self.x += ENEMY_XDELTA

    def move_vertical(self):
        self.y += ENEMY_YDELTA

class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/laser.png')
        self.rect = self.image.get_rect()
        self.laser_state = LASER_STATE
        self.x = LASER_X
        self.y = LASER_Y
        self.x_change = 0
        self.y_change = 15

    def fire_laser(self,ShipX):
        global LASER_X
        if LASER_STATE is "ready":
            laserSound = mixer.Sound("sounds/laser.wav")
            laserSound.play()
            # Get the current x coordinate of the spaceship
            LASER_X = ShipX
        screen.blit(Laser.image, (LASER_X + 16, LASER_Y + 10))

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
        self.x = MOON_X
        self.y = MOON_Y

    def displayMoon(self):
        screen.blit(self.image, self.x, self.y)

def main():
    # make caption for the window and add an icon
    global LASER_STATE, LASER_Y
    pygame.display.set_caption("Hicks Space Invaders")
    icon = pygame.image.load('images/moon.png')
    pygame.display.set_icon(icon)
    Moon.displayMoon()

    playing = True
    while playing:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        Moon.displayMoon()

        for event in pygame.event.get():  # end the game if you quit
            if event.type == pygame.QUIT:
                playing = False
                # if keystroke is pressed check whether its right or left
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        Ship.move_left()
                    if event.key == pygame.K_RIGHT:
                        Ship.move_right()
                    if event.key == pygame.K_SPACE:  # shoot laser with spacebar
                        if LASER_STATE is "ready":
                            laserSound = mixer.Sound("sounds/laser.wav")
                            laserSound.play()
'''
        # Enemy Movement
        for i in range(NUM_ENEMIES):

            # Game Over
            if Enemy[i] > 440:
                for j in range(NUM_ENEMIES):
                    Enemy[j] = 2000
                game_over_text()
                break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 4
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -4
                enemyY[i] += enemyY_change[i]

            # Collision
            collision = isCollision(enemyX[i], enemyY[i], LASER_X, LASER_Y)
            if collision:
                LASER_Y= 480
                LASER_STATE = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)

            enemy(enemyX[i], enemyY[i], i)

        # laser Movement
        if LASER_Y <= 0:
            LASER_Y = 480
            LASER_STATE = "ready"
    # firing the laser
        if LASER_STATE is "fire":
            Laser.fire_laser()
            LASER_Y = LASER_Y - LASER_DELTA
'''

    Ship.showShip()
    show_score()
    pygame.display.update()
    fpsClock.tick(FPS)

if __name__ == "__main__":
        main()