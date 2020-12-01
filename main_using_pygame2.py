# Portions of coded modified from the link below
# Sounds taken from github file
# https://github.com/attreyabhatt/Space-Invaders-Pygame

import pygame
from sprites import Ship, Laser, Moon, Enemy, Kill
from api_test import current_moonphase

NUM_ENEMIES = 24


MAX_LASERS = 3

SHIP_X = 380
SHIP_Y = 520


LASER_X = 0
LASER_Y = 480
LASER_DELTA = 20

ENEMY_Y_DELTA = 40
ENEMY_X_DELTA = 4


titleImg = pygame.image.load('images/spaceinvaders_title.png')
title_x = 210
title_y = 40

HEIGHT = 600
WIDTH = 800

pygame.init()
clock = pygame.time.Clock()
FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load('images/background.png')
kill = pygame.image.load('images/kill.png')

# Score
score_value = 0
font = pygame.font.Font('font/space_invaders.ttf', 22)
# game over
game_over_font = pygame.font.Font('font/space_invaders.ttf', 50)


def show_score():
    text_x = 10
    text_y = 10
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (text_x, text_y))

def game_over_text():
    game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over_text, (250, 500))

def title(x, y):
    titleImg = pygame.image.load('images/spaceinvaders_title.png')
    screen.blit(titleImg, (x, y))

def main():
    playing = True
    kill_time = 0
    score_value = 0
    SHIP_LIVES = 0
    pygame.display.set_caption("Hicks Space Invaders")
    icon = pygame.image.load('images/ship.png')
    pygame.display.set_icon(icon)


    moon = Moon(current_moonphase)
    ship = Ship(SHIP_X,SHIP_Y)
    kill = Kill()
    laser = Laser(LASER_X,LASER_Y)
    enemies = pygame.sprite.Group()
    lasers = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    title(title_x, title_y)

    def makeEnemies():
        for i in range(NUM_ENEMIES):
            image_name = "images/enemy%d.png" % (i % 4)
            mod = (i % 4)
            row = mod
            if i < 4:
                col = 1
            elif i < 8:
                col = 2
            elif i < 12:
                col = 3
            elif i < 16:
                col = 4
            elif i < 20:
                col = 5
            elif i < 24:
                col = 6
            enemy = Enemy(image_name, row, col)
            enemies.add(enemy)
    makeEnemies()
    all_sprites.add(enemies)
    all_sprites.add(laser)
    all_sprites.add(ship)
    all_sprites.add(moon)
    all_sprites.draw(screen)

    while playing:

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
                    if len(lasers.sprites()) < MAX_LASERS:
                        new_laser = Laser(ship.rect.centerx,ship.rect.centery)
                        new_laser.laser_speed = -LASER_DELTA
                        lasers.add(new_laser)
                        laser_sound = pygame.mixer.Sound("sounds/laser.wav")
                        laser_sound.play()
            if event.type == pygame.KEYUP and not event.key == pygame.K_SPACE:
                ship.stop()

        ship.update()
        lasers.update()

        for laser in lasers.sprites():
            if laser.rect.bottom < 0:
                laser.kill()

        enemies.update()
        for enemy in enemies.sprites():
            if enemy.rect.left < 0:
                enemy.rect.left = 0
                enemy.x_speed *= -1
                enemy.rect.y += 30

            if enemy.rect.right > WIDTH:
                enemy.rect.right = WIDTH
                enemy.x_speed *= -1
                enemy.rect.y += 30

        if ship.rect.left <= 0:
            ship.rect.left = 0
        elif ship.rect.right >= 736:
            ship.rect.right = 736

        # keep enemies in bounds
        laser_collisions = pygame.sprite.groupcollide(lasers,enemies,True,True)

        if kill_time > 30:
            kill.kill()
            kill_time = 0


        if laser_collisions:
            all_sprites.add(kill)
            print(score_value)


        score_value += len(laser_collisions)

        collisions = pygame.sprite.spritecollide(ship,enemies,False)


        if len(collisions) > 0:
            SHIP_LIVES -= 1
            collisions[0].kill()

        if len(enemies) == 0:
            makeEnemies()
            enemies.draw(screen)

        kill_time += 1
        screen.blit(background, (0, 0))

        lasers.draw(screen)

        all_sprites.draw(screen)
        show_score()
        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == "__main__":
        main()
