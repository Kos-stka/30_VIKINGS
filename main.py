import pygame as pg
import constants

from hero_erik import Erik
from level_01 import Level01

GROUND = 660

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), pg.HWSURFACE)
        self.clock = pg.time.Clock()
        pg.time.set_timer(pg.USEREVENT, 2000)

        pg.display.set_caption("The Lost Vikings")
        pg.display.set_icon(pg.image.load("images/vikings_icon.jpeg").convert())

        self.gameRunning = True
        self.playing = True
        self.climbing = False

        # load Heroes
        self.heroes = pg.sprite.Group()
        self.heroes.add(Erik(100, GROUND+2))
        self.player = self.heroes.sprites()[0]
        self.player.status = constants.HERO_STATUS_STANDING
        # self.player.status = constants.HERO_STATUS_FALLING

        self.level = Level01(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

    def render(self):
        self.screen.fill(constants.BLACK)

        self.screen.blit(self.level.background, self.level.rect)
        if self.player.status == constants.HERO_STATUS_FALLING:
            self.heroes.update(self.isOnPlatform())
        else:
            self.heroes.update(None)
        self.heroes.draw(self.screen)
        # self.screen.blit(self.level.foreground, self.level.rect)
        
        pg.draw.circle(self.screen, constants.RED, (60, GROUND-180-12), 4)  # platform up
        pg.draw.circle(self.screen, constants.RED, (20, GROUND), 4)   # plstform mid
        pg.draw.circle(self.screen, constants.RED, (92, GROUND-180-32-12), 4)   # ladder
        # pg.draw.rect(self.screen, constants.BLUE, (60, 180, 10*32, 3*32), 2)
        # pg.draw.rect(self.screen, constants.BLUE, (20, 360, 30*32, 3*32), 2)
        # pg.draw.rect(self.screen, constants.GREEN, (100, GROUND, 2*32, 2*32), 2)
        pg.draw.circle(self.screen, constants.RED, (100, GROUND), 4)   # erik start point
        # pg.draw.rect(self.screen, constants.BLUE, (92, GROUND-180-32-12), 2)

        pg.display.update()

    def isOnPlatform(self):
        rect = self.player.rect
        rect.bottom = rect.bottom -2
        rect.y += 2
        onPlatform = pg.sprite.spritecollide(self.player, self.level.platform_list, False)
        if len(onPlatform):
            self.player.status = constants.HERO_STATUS_STANDING
            return onPlatform[0]
        else:
            self.player.status = constants.HERO_STATUS_FALLING
            return None

    def events(self, event):
        if event.type == pg.QUIT:
            self.gameRunning = False
        elif event.type == pg.KEYDOWN:
            if self.playing:
                if event.key == pg.K_LEFT:
                    if self.player.status == constants.HERO_STATUS_CLIMBING:
                        self.player.doStopClimbing()
                        self.player.status = constants.HERO_STATUS_FALLING
                        self.climbing = False
                    # self.player.status = constants.HERO_STATUS_WALKING # or FALLING
                    self.player.goLeft(self.isOnPlatform())
                    
                elif event.key == pg.K_RIGHT:
                    if self.player.status == constants.HERO_STATUS_CLIMBING:
                        self.player.doStopClimbing()
                        self.player.status = constants.HERO_STATUS_FALLING
                        self.climbing = False
                    # self.player.status = constants.HERO_STATUS_WALKING # or FALLING
                    self.player.goRight(self.isOnPlatform())

                elif event.key == pg.K_UP:
                    if self.climbing:
                        self.climbing = self.player.goClimbUp()
                        self.player.status = constants.HERO_STATUS_CLIMBING
                    else:
                        onPlatform = pg.sprite.spritecollide(self.player, self.level.ladder_list, False)
                        if len(onPlatform) > 0:
                            self.player.status = constants.HERO_STATUS_CLIMBING
                            self.climbing = self.player.goClimbUp(onPlatform[0])
                elif event.key == pg.K_DOWN:
                    if self.climbing:
                        self.climbing = self.player.goClimbDown()
                        self.player.status = constants.HERO_STATUS_CLIMBING
                    else:
                        onPlatform = pg.sprite.spritecollide(self.player, self.level.ladder_list, False)
                        if len(onPlatform) > 0:
                            self.player.status = constants.HERO_STATUS_CLIMBING
                            self.climbing = self.player.goClimbDown(onPlatform[0])

                elif event.key == pg.K_SPACE:
                    self.climbing = False
                    self.player.status = constants.HERO_STATUS_JUMPING
                    self.player.doActionOne(GROUND+2)
        elif event.type == pg.KEYUP:
            if self.playing:
                if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                    self.player.doStopRunning()
                    self.player.status = constants.HERO_STATUS_STANDING
                if event.key == pg.K_UP or event.key == pg.K_DOWN:
                    self.player.doStopClimbing()
                    self.player.status = constants.HERO_STATUS_CLIMBING

    def execute(self):
        while self.gameRunning:
            self.render()
            for event in pg.event.get():
                self.events(event)
            self.clock.tick(constants.FPS)

game = Game()
game.execute()

print("Goobye...")