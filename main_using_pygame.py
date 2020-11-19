import random
import pygame
from pygame import mixer

from api_test import current_moonphase

NUM_ENEMIES = 12
enemies = []
BLOCKSIZE = 100

pygame.init()
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('images/background.png')

# Score
score_value = 0
font = pygame.font.Font('font/space_invaders.ttf', 22)
# game over
game_over_font = pygame.font.Font('font/space_invaders.ttf', 50)


def show_score(x,y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text(x,y):
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
        self.move_x = 0  # move along X
        self.frame = 0  # count frames
    def display_Ship(self, x, y):
        screen.blit(self.image, self.x, self.y)
    def control(self,x):
        self.move_x += x


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
    def move(self,x,y):
        self.move_x += x
        self.move_y += y

class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/laser.png')
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 480
        self.x_change = 0
        self.y_change = 15
        self.state = "ready"
    def fire_laser(self,x,y):
        self.state = "fire"
        screen.blit(Laser.image, (x + 16, y + 10))
    def display_Laser(self,x,y):
        screen.blit(self.image, self.x, self.y)

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
    def displayMoon(self):
        screen.blit(self.image, self.x, self.y)

def main():
    # make caption for the window and add an icon
    pygame.display.set_caption("Hicks Space Invaders")
    icon = pygame.image.load('images/moon.png')
    pygame.display.set_icon(icon)


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
                        Ship.control()
                    if event.key == pygame.K_RIGHT:
                        player.X_change = 6
                    if event.key == pygame.K_SPACE:  # shoot laser with spacebar
                        if laser_state is "ready":
                            laserSound = mixer.Sound("sounds/laser.wav")
                            laserSound.play()
                            # Get the current x cordinate of the spaceship
                            laserX = playerX
                            fire_laser(laserX, laserY)
                            Laser.



if __name__ == "__main__":
        main()