import pygame
import constants

class spritesheet(object):
    def __init__(self, filename, colorkey = None):
        try:
            self.colorkey = None
            self.sheet = pygame.image.load(filename).convert()
            # self.sheet.set_colorkey((104,0,152))
            if colorkey != None:
                if colorkey == -1:
                    colorkey = self.sheet.get_at((0,0))
                self.sheet.set_colorkey(colorkey, pygame.RLEACCEL)
                self.colorkey = constants.BLACK

        except pygame.error as message:
            print('Unable to load spritesheet image:', filename)
            raise SystemExit(message)

    # Load a specific image from a specific rectangle x,y,x+W,y+H
    def load_sprite(self, x, y, W=constants.HERO_W, H = constants.HERO_H):
        rect = pygame.Rect((x,y,W,H))
        sprite_surf = pygame.Surface(rect.size).convert()  # not convert_alpha
        # sprite_surf.fill(constants.BLUE)
        sprite_surf.blit(self.sheet, (0,0), rect)

        if self.colorkey != None or self.colorkey != -1:
            sprite_surf.set_colorkey(self.colorkey, pygame.RLEACCEL)

        sprite_surf = pygame.transform.scale2x(sprite_surf)
        return sprite_surf

    # Load a whole bunch of images and return them as a list
    def load_sprites(self, start_x, start_y, sprite_count=1 ,W=constants.HERO_W, H = constants.HERO_H):
        sprites = []
        for i in range(sprite_count):
            sprites.append(self.load_sprite(start_x + i * W, start_y, W, H))
        return sprites

    # Load a specific image from a specific rectangle x,y,x+offset,y+offset
    def image_at(self, rectangle, colorkey = None):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
            # if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
