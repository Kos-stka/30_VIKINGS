import pygame
import constants

class AnimSprite(object):
    def __init__(self, images, animLen, animFrames = None, animInterval = None):
        # ss.load_sprites(9, 363, 3, W=constants.HERO_W-1), length=105, [0,1,2,1,2,1,0]
        self.images = images
        self.animLen = animLen
        self.index = 0

        self.frames = None
        self.interval = 0
        if animFrames is not None:
            self.frames = animFrames
            self.interval = self.animLen // len(self.frames)
        elif animInterval is not None:
            self.frames = animInterval
            self.interval = 0
        else:
            self.frames = range(len(images))
            self.interval = self.animLen // len(self.frames)

    def start(self):
        self.index = 0

    def reset(self):
        self.index = 0

    def getAt(self, i = 0):
        return self.images[0]

    def curr(self, left = False ):
        image = self.images[self.index % len(self.images)]
        if left: image = pygame.transform.flip(image, 1, 0)
        return image

    def prev(self, left = False ):
        self.index -= 1
        if self.index < 0:
            self.index = self.animLen

        frame_index = 0
        if self.interval:
            image_index = ( self.index // self.interval ) % len(self.frames)
            frame_index = self.frames[image_index] % len(self.images)
        else:
            for ind, val in enumerate(self.frames):
                if self.index < val:
                    frame_index = ind
                    break

        image = self.images[frame_index]
        if left: image = pygame.transform.flip(image, 1, 0)
        return image

    def next(self, left = False ):
        self.index = ( self.index + 1 ) % self.animLen

        frame_index = 0
        if self.interval:
            image_index = ( self.index // self.interval ) % len(self.frames)
            frame_index = self.frames[image_index] % len(self.images)
        else:
            for ind, val in enumerate(self.frames):
                if self.index < val:
                    frame_index = ind
                    break

        image = self.images[frame_index]
        if left: image = pygame.transform.flip(image, 1, 0)
        return image