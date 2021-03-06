# Portions of coded modified from the link below
# Sounds taken from github file
# https://github.com/attreyabhatt/Space-Invaders-Pygame

import math
import random
import time
import pygame

from pygame import mixer
from api_test import current_moonphase

# Initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Load in the background
background = pygame.image.load('images/background.png')


# make caption for the window and add an icon
pygame.display.set_caption("Hicks Space Invaders")
icon = pygame.image.load('images/ship.png')
pygame.display.set_icon(icon)

# create a player and initialize location
playerImg = pygame.image.load('images/ship.png')
playerX = 380
playerY = 520
playerX_change = 0

# create moon and initialize location
if current_moonphase == 'New Moon':
    moonImg = pygame.image.load('images/newmoon.png')

if current_moonphase == 'Waxing Crescent':
    moonImg = pygame.image.load('images/waxingcrescent.png')

if current_moonphase == 'First Quarter':
    moonImg = pygame.image.load('images/firstquarter.png')

if current_moonphase == 'Waxing Gibbous':
    moonImg = pygame.image.load('images/waxinggibbous.png')

if current_moonphase == 'Full Moon':
    moonImg = pygame.image.load('images/fullmoon.png')

if current_moonphase == 'Waning Gibbous':
    moonImg = pygame.image.load('images/waninggibbous.png')

if current_moonphase == 'Last Quarter':
    moonImg = pygame.image.load('images/lastquarter.png')

if current_moonphase == 'Waning Crescent':
    moonImg = pygame.image.load('images/waningcrescent.png')

moonX = 660
moonY = 35
moonX_change = 0

titleImg = pygame.image.load('images/spaceinvaders_title.png')
titlex = 210
titley = 40

# create enemies on the screen
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_enemies = 12

for i in range(num_enemies):
    if i % 4 == 0:
        enemy = 'images/enemy0.png'
    elif i % 4 == 1:
        enemy = 'images/enemy1.png'
    elif i % 4 == 2:
        enemy = 'images/enemy2.png'
    else:
        enemy = 'images/enemy3.png'
    enemyImg.append(pygame.image.load(enemy))
    enemyX.append(random.randint(10, 750))
    enemyY.append(random.randint(60, 250))
    enemyX_change.append(4)
    enemyY_change.append(35)


# laser code
laserImg = pygame.image.load('images/laser.png')
laserX = 0
laserY = 480
laserX_change = 0
laserY_change = 15
laser_state = "ready"


# Score
score_value = 0
font = pygame.font.Font('font/space_invaders.ttf', 22)

textX = 10
textY = 10

# game over
game_over_font = pygame.font.Font('font/space_invaders.ttf', 50)

def timer(start_time):          # needs to be fixed so that it creates a running timer from 60 seconds
    time_remaining = 60 - (start_time - time.time())
    timer_x = 300
    timer_y = 5
    if time_remaining >= 0:
        timer_text = font.render("Time Remainng: " + str(time_remaining), True, (255, 255, 255))
        screen.blit(timer_text,(timer_x,timer_y))

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over_text, (200, 250))

def title(x, y):
    screen.blit(titleImg, (x, y))

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
    if distance < 27:
        return True
    else:
        return False

def isCollision_moon(moonX, moonY, laserX, laserY):        # looked up collision logic for this
    distance = math.sqrt(math.pow(moonX - laserX, 2) + (math.pow(moonY - laserY, 2)))
    if distance < 27:
        return True
    else:
        return False


# loop to play game
playing = True
while playing:
    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    moon(moonX, moonY)
    title(titlex,titley)
    for event in pygame.event.get():        # end the game if you quit
        if event.type == pygame.QUIT:
            playing = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -6
            if event.key == pygame.K_RIGHT:
                playerX_change = 6
            if event.key == pygame.K_SPACE: # shoot laser with spacebar
                if laser_state is "ready":
                    laserSound = mixer.Sound("sounds/laser.wav")
                    laserSound.play()
                    # Get the current x cordinate of the spaceship
                    laserX = playerX
                    fire_laser(laserX, laserY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    for i in range(num_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_enemies):
                enemyY[j] = 2000
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
        collision = isCollision(enemyX[i], enemyY[i], laserX, laserY)
        if collision:
            laserY = 480
            laser_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # laser Movement
    if laserY <= 0:
        laserY = 480
        laser_state = "ready"

    if laser_state is "fire":
        fire_laser(laserX, laserY)
        laserY -= laserY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()