import pygame
import constants
import spritesheet

class Decor(pygame.sprite.Sprite):
    def __init__(self, tiles, x, y, W = 3, H = 2, type = ""):
        super(Decor, self).__init__()

        self.image = pygame.Surface((2*W * constants.MAP_TILE_W, 2 * H * constants.MAP_TILE_H)).convert()
        # self.image.set_colorkey(constants.BLACK, pygame.RLEACCEL)
        # self.image.fill(constants.BLACK)
        
        pos_X = 2 * constants.MAP_TILE_W
        pos_Y = 2 * constants.MAP_TILE_H
        if type == "mushroom_red1": 
            self.image.blit(tiles[5][20], (      0,     0))
            self.image.blit(tiles[5][21], (  pos_X,     0))
            self.image.blit(tiles[5][22], (2*pos_X,     0))
            self.image.blit(tiles[6][ 0], (  pos_X, pos_Y))
            self.image.blit(tiles[6][ 1], (2*pos_X, pos_Y))
        elif type == "mushroom_red2":
            self.image.blit(tiles[7][0], (      0,     0))
            self.image.blit(tiles[7][1], (  pos_X,     0))
            self.image.blit(tiles[7][2], (2*pos_X,     0))
            self.image.blit(tiles[7][6], (      0, pos_Y))
            self.image.blit(tiles[7][7], (  pos_X, pos_Y))
        elif type == "mushroom_blue1":
            self.image.blit(tiles[5][7], (      0,     0))
            self.image.blit(tiles[5][8], (  pos_X,     0))
            self.image.blit(tiles[5][9], (2*pos_X,     0))
            self.image.blit(tiles[5][14], (     0, pos_Y))
            self.image.blit(tiles[5][15], ( pos_X, pos_Y))
        elif type == "mushroom_blue2":
            self.image.blit(tiles[5][11], (      0,     0))
            self.image.blit(tiles[5][12], (  pos_X,     0))
            self.image.blit(tiles[5][13], (2*pos_X,     0))
            self.image.blit(tiles[5][18], (  pos_X, pos_Y))
            self.image.blit(tiles[5][19], (2*pos_X, pos_Y))
        elif type == "mushroom_yellow1":
            self.image.blit(tiles[14][22], (     0,     0))
            self.image.blit(tiles[15][0], (  pos_X,     0))
            self.image.blit(tiles[15][1], (2*pos_X,     0))
            self.image.blit(tiles[15][2], (      0, pos_Y))
            self.image.blit(tiles[15][3], (  pos_X, pos_Y))
            self.image.blit(tiles[15][4], (2*pos_X, pos_Y))
        elif type == "mushroom_yellow2":
            self.image.blit(tiles[6][2], (      0,     0))
            self.image.blit(tiles[6][3], (  pos_X,     0))
            self.image.blit(tiles[6][4], (2*pos_X,     0))
            self.image.blit(tiles[6][5], (      0, pos_Y))
            self.image.blit(tiles[6][6], (  pos_X, pos_Y))
            self.image.blit(tiles[6][7], (2*pos_X, pos_Y))
            
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
