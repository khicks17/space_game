import pygame
import string
from typing import Tuple
import colors




class GameBoard(pygame.sprite.Sprite):

    def __init__(self, dimension, surface):
        super().__init__()
        self.image = pygame.Surface(dimension)
        self.image.convert()
        self.rect = self.image.get_rect()

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # helper variables for spacing sprite images
        self.x_step = self.width // NBLOCKS
        self.y_step = self.height // NBLOCKS

        # location where the board is drawn (the actual window)
        self.surface = surface

    def initialize(self):
        # Draw board background use color [board_bkgd]
        self.image.fill(colors.board_bkgd)

        # Draw border around the board use color [foreground]
            pygame.draw.line(self.image, [0, 0, 0], [0,0], [329,0])         #top left to top right
            pygame.draw.line(self.image, [0, 0, 0], [0,0], [0,329])         #top left to bottom left

            pygame.draw.line(self.image, [0, 0, 0], [329, 329], [329, 0])   #bottom right to top right
            pygame.draw.line(self.image, [0, 0, 0], [329, 329], [0, 329])   #bottom right to bottom left
        # --------- END YOUR CODE ------------

    def draw(self):
        self.surface.blit(self.image, (self.rect.x, self.rect.y))

    def add_sprite(self, sprite: pygame.Surface, loc: Tuple[int, int]):

        row = loc[0]
        col = loc[1]
        x = self.x_step * (col + 1)
        y = self.y_step * (row + 1)
        self.image.blit(sprite, (x, y))
