import pygame
import constants
import spritesheet

from map_platform import Platform
from map_ladder import Ladder
from map_decor import Decor

class Level01(pygame.sprite.Sprite):
    def __init__(self, W, H):
        super(Level01, self).__init__()

        ss = spritesheet.spritesheet("images/LV_LLM0.png", constants.BLACK)
        tiles = []
        for i in range(32):
            tiles.append(ss.load_sprites(0, i*16, 23, W=16, H=16))

        self.background = pygame.Surface((W, H)).convert()
        self.background.fill(constants.BLACK)

        self.foreground = pygame.Surface((W, H)).convert()
        # self.foreground.fill(constants.BLACK)

        # draw platform
        LEVEL_GROUND = 660

        # set platforms
        self.platform_list = pygame.sprite.Group()
        self.platform_list.add(Platform(tiles, 60, LEVEL_GROUND-180-12, 10, 3))
        self.platform_list.add(Platform(tiles, 20, LEVEL_GROUND, 30, 3))

        # set ladders
        self.ladder_list = pygame.sprite.Group()
        self.ladder_list.add(Ladder(tiles, 92, LEVEL_GROUND-180-32-12, 2, 7))

        # add decors
        self.decor_list = pygame.sprite.Group()
        self.decor_list.add(Decor(tiles, 160, LEVEL_GROUND-2*32, type="mushroom_red2"))
        self.decor_list.add(Decor(tiles, 288, LEVEL_GROUND-2*32, type="mushroom_red1"))

        self.decor_list.add(Decor(tiles, 160, LEVEL_GROUND-180-12-2*32, type="mushroom_blue1"))
        self.decor_list.add(Decor(tiles, 288, LEVEL_GROUND-180-12-2*32, type="mushroom_blue2"))

        self.decor_list.add(Decor(tiles, 416, LEVEL_GROUND-2*32, type="mushroom_yellow1"))
        self.decor_list.add(Decor(tiles, 544, LEVEL_GROUND-2*32, type="mushroom_yellow2"))

        self.platform_list.draw(self.background)
        self.ladder_list.draw(self.background)

        # self.decor_list.draw(self.foreground)
        self.decor_list.draw(self.background)

        self.rect = self.background.get_rect()
