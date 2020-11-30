# Portions of coded modified from the link below
# Sounds taken from github file
# https://github.com/attreyabhatt/Space-Invaders-Pygame

import random
import pygame
from pygame import mixer
from sprites import Ship, Enemy, Laser, Moon
from api_test import current_moonphase

NUM_ENEMIES = 12
enemies = []
BLOCKSIZE = 100


LASER_X = 0
LASER_Y = 480
LASER_STATE = "ready"
LASER_DELTA = 15

ENEMY_Y_DELTA = 40
ENEMY_X_DELTA = 4

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


def main():
    pygame.display.set_caption("Hicks Space Invaders")
    icon = pygame.image.load('images/moon.png')
    pygame.display.set_icon(icon)

    moon = Moon(current_moonphase)
    ship = Ship()
    laser = Laser()
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

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

    playing = True
    while playing:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(ship,ship.x,ship.y)
        screen.blit(moon,moon.x,moon.y)
        screen.blit(enemy,enemy.x,enemy.y)



        all_sprites.draw(screen)
        show_score()
        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == "__main__":
        main()