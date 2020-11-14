import math
import random

import pygame
from pygame import mixer
from api_test import current_moonphase

# Initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((1920, 1080))          #1920x1080 is size of laptop

# Load in the background
background = pygame.image.load('background.png')

# make caption for the window and add an icon
pygame.display.set_caption("Hicks Space Invaders")
icon = pygame.image.load('fullmoon.png')
pygame.display.set_icon(icon)

# create a player and initialize location
playerImg = pygame.image.load('ship.png')
playerX = 1920/2
playerY = 400
playerX_change = 0

# create moon and initialize location
if current_moonphase == 'New Moon':
    moonImg = pygame.image.load('newmoon.png')

if current_moonphase == 'Waxing Crescent':
    moonImg = pygame.image.load('waxingcrescent.png')

if current_moonphase == 'First Quarter':
    moonImg = pygame.image.load('firstquarter.png')

if current_moonphase == 'Waxing Gibbous':
    moonImg = pygame.image.load('waxinggibbous.png')

if current_moonphase == 'Full Moon':
    moonImg = pygame.image.load('fullmoon.png')

if current_moonphase == 'Waning Gibbous':
    moonImg = pygame.image.load('waninggibbous.png')

if current_moonphase == 'Last Quarter':
    moonImg = pygame.image.load('lastquarter.png')

if current_moonphase == 'Waning Crescent':
    moonImg = pygame.image.load('waningcrescent.png')
moonX = 1920/2
moonY = 40
moonX_change = 0

# create enemies on the screen
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_enemies = 6

# laser code
# Ready - You can't see the laser on the screen
# Fire - The bullet is currently moving

laserImg = pygame.image.load('laser.png')
laserX = 0
laserY = 480
laserX_change = 0
laserY_change = 10
laser_state = "ready"

for i in range(num_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)


# Score
score_value = 0
font = pygame.font.Font('space_invaders.ttf', 32)

# game over
game_over_font = pygame.font.Font('space_invaders.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def moon(x, y):
    screen.blit(moonImg, (x, y))

def fire_laser(x, y):
    global laser_state                                  # looked up use of global
    laser_state = "fire"
    screen.blit(laserImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, laserX, laserY):        # looked up collision logic for this
    distance = math.sqrt(math.pow(enemyX - laserX, 2) + (math.pow(enemyY - laserY, 2)))
    if distance < 25:
        return True
    else:
        return False