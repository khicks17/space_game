# Portions of coded modified from the link below
# Sounds taken from github file
# https://github.com/attreyabhatt/Space-Invaders-Pygame

import random
import pygame
from pygame import mixer
from sprites import Ship, Laser, Moon, Enemy
from api_test import current_moonphase
from random import randint

NUM_ENEMIES = 12
BLOCKSIZE = 100

SHIP_X = 380
SHIP_Y = 520
SHIP_X_DELTA = 6

LASER_X = 0
LASER_Y = 480
LASER_STATE = "ready"
LASER_DELTA = 15

ENEMY_Y_DELTA = 40
ENEMY_X_DELTA = 4

MOON_X = 660
MOON_Y = 35

titleImg = pygame.image.load('images/spaceinvaders_title.png')
title_x = 210
title_y = 40

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



def main():
    global playing
    playing = True
    pygame.display.set_caption("Hicks Space Invaders")
    icon = pygame.image.load('images/moon.png')
    pygame.display.set_icon(icon)

    moon = Moon(current_moonphase)
    ship = Ship(SHIP_X,SHIP_Y)
    laser = Laser(LASER_X,LASER_Y)
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    title(title_x, title_y)

    for i in range(NUM_ENEMIES):
        image_name = "images/enemy%d.png" % (i % 4)
        row = (i % 6)
        col = i
        enemy = Enemy(image_name, row, col)
        enemies.add(enemy)
        all_sprites.add(enemy)
    all_sprites.add(ship)
    all_sprites.add(moon)
    all_sprites.add(laser)


    while playing:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(ship,ship.x,ship.y)
        screen.blit(moon,moon.x,moon.y)

        for each in enemies
            for i in range(NUM_ENEMIES)
                e_row = i
                e_col = i
                screen.blit(each, e_row*(BLOCKSIZE + 100), e_col*(BLOCKSIZE + 20))

        for event in pygame.event.get():        # end the game if you quit
            if event.type == pygame.QUIT:
                playing = False

            # if keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ship.move_left()
                if event.key == pygame.K_RIGHT:
                    ship.move_right()
                if event.key == pygame.K_SPACE: # shoot laser with spacebar
                    if laser.laser_state is "ready":
                        laserSound = mixer.Sound("sounds/laser.wav")
                        laserSound.play()
                        # Get the current x coordinate of the spaceship
                        laser.x = ship.x
                        laser.fire_laser(laser.x,laser.y)

          ''''  if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0
            '''


        ship.x += SHIP_X_DELTA
        if ship.x <= 0:
            ship.x = 0
        elif ship.x >= 736:
            ship.x = 736

        # Enemy Movement
        for i in range(NUM_ENEMIES):

            # Game Over
            if enemyY[i] > 440:
                for j in range(NUM_ENEMIES):
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
                laser.y = 480
                laser.laser_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)

            enemy(enemyX[i], enemyY[i], i)

        # laser Movement
        if laserY <= 0:
            laserY = 480
            laser_state = "ready"

        if laser.laser_state is "fire":
            laser.fire_laser(laser.x, laser.y)
            laser.y -= LASER_DELTA









''''
        all_sprites.draw(screen)
        show_score()
        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == "__main__":
        main()
