import pygame
import constants
import spritesheet

class Ladder(pygame.sprite.Sprite):
    def __init__(self, tiles, x, y, W = 2, H = 5, type = 0):
        super(Ladder, self).__init__()

        self.image = pygame.Surface((2*W * constants.MAP_TILE_W, 2 * H * constants.MAP_TILE_H)).convert()
        self.image.fill(constants.BLACK)
        
        pos_X = 2 * constants.MAP_TILE_W
        # draw lagger
        for i in range(H):
            pos_Y = (i) * 2 * constants.MAP_TILE_H
            # green grass
            if i == 0: # Ladder top
                for x_i in [0, 1]:
                    self.image.blit(tiles[5][16 + x_i], (x_i * pos_X, pos_Y))
            elif i == 1: # Ladder over grass
                for x_i in [0, 1]:
                    self.image.blit(tiles[0][ 8 + x_i], (x_i * pos_X, pos_Y))
            elif i == 2: # Ladder over sand
                for x_i in [0, 1]:
                    self.image.blit(tiles[30][16 + x_i], (x_i * pos_X, pos_Y))
            elif i == 3: # Ladder over sand end
                for x_i in [0, 1]:
                    self.image.blit(tiles[28][19 + x_i], (x_i * pos_X, pos_Y))
            else: # Ladder on open air
                for x_i in [0, 1]:
                    self.image.blit(tiles[0][6 + x_i], (x_i * pos_X, pos_Y))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
