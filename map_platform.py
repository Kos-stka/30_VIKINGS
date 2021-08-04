import pygame
import constants
import spritesheet

class Platform(pygame.sprite.Sprite):
    def __init__(self, tiles, x, y, W, H, type = 0):
        super(Platform, self).__init__()

        ss = spritesheet.spritesheet("images/LV_LLM0.png", constants.BLACK)

        self.image = pygame.Surface((2*W * constants.MAP_TILE_W, 2 * H * constants.MAP_TILE_H)).convert()
        self.image.fill(constants.BLACK)

        # draw platform
        for i in range(W):
            pos_X = i * 2 * constants.MAP_TILE_W
            pos_earth_y = 2 * constants.MAP_TILE_H
            pos_bottom_y = 4 * constants.MAP_TILE_H
            # green grass
            if i == 0:
                self.image.blit(tiles[0][2], (pos_X, 0))
            elif i == W-1:
                self.image.blit(tiles[3][12], (pos_X, 0))
            else:
                self.image.blit(tiles[3][13+i%3], (pos_X, 0))

            # brown eatrh
            if i % 3 == 0:
                self.image.blit(tiles[0][22], (pos_X, pos_earth_y))
            elif i % 3 == 1:
                self.image.blit(tiles[1][0], (pos_X, pos_earth_y))
            elif i % 3 == 2:
                self.image.blit(tiles[1][4], (pos_X, pos_earth_y))
            else:
                self.image.blit(tiles[1][5], (pos_X, pos_earth_y))

            # # end of braun earth
            self.image.blit(tiles[28][21+i%2], (pos_X, pos_bottom_y))
            # self.image.blit(self.tiles[1][22], (i*16*2, PLATFORM_GROUND+32*4))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

