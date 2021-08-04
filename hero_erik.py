import pygame
import constants
import spritesheet
import spriteanim

class Erik(pygame.sprite.Sprite):
    def __init__(self, x = 0, y = 0):
        super(Erik, self).__init__()

        ss = spritesheet.spritesheet("images/erik.png", -1)

        self.sprite_stand = spriteanim.AnimSprite(
            ss.load_sprites(5, 5, 2, W=constants.HERO_W - 1), 
            constants.ERIK_STAND_BLINK_TIME, 
            animInterval=[
                constants.ERIK_STAND_BLINK_TIME - constants.ERIK_STAND_BLINK_DELAY, 
                constants.ERIK_STAND_BLINK_TIME])

        sprite_running = ss.load_sprites(6, 114, 8)
        self.running_interval = constants.ERIK_WALK_SPEED * len(sprite_running)
        self.sprite_running = spriteanim.AnimSprite(sprite_running, self.running_interval)

        self.sprite_stoping = spriteanim.AnimSprite(ss.load_sprites(6, 249, 3, W=constants.HERO_W-1), 130, [2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2])
        self.sprite_jumping = spriteanim.AnimSprite(ss.load_sprites(6, 212, 4), 2 * constants.ERIK_JUMP_FORCE, animInterval=constants.ERIK_JUMP_INTERVAL)
        self.sprite_falling = spriteanim.AnimSprite(ss.load_sprites(80, 212, 2), 40)
        self.sprite_tying = spriteanim.AnimSprite(ss.load_sprites(9, 363, 3, W=constants.HERO_W-1), 105, [0,1,2,1,2,1,0])
        self.sprite_climbing = spriteanim.AnimSprite(ss.load_sprites(4, 288, 4), 40)

        self.image = self.sprite_stand.getAt()
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y
        self.jumpGround = y
        self.index = 0
        self.running_time = 0
        self.stopping = -1
        self.jumpMove = constants.ERIK_JUMP_FORCE + 1
        self.lastMoveLeft = self.moveLeft = self.moveRight = False

        self.status = constants.HERO_STATUS_STANDING

        self.onLadder = False
        self.doClimbing = False
        self.climbingUp = False

        self.rect.x = self.x
        # self.rect.y = self.y
        self.rect.bottom = self.y

    def isFalling(self):
        if self.status == constants.HERO_STATUS_FALLING:
            self.y += constants.ERIK_JUMP_FORCE // 4

    def goLeft(self, platform = None):
        self.onLadder = False
        self.x -= constants.ERIK_WALK_SPEED
        self.isFalling()
        self.moveLeft = self.lastMoveLeft= True
        self.index = 0

        if platform != None:
            self.y = platform.rect.y + 2
            self.jumpGround = platform.rect.y + 2

    def goRight(self, platform = None):
        self.onLadder = False
        self.x += constants.ERIK_WALK_SPEED
        self.isFalling()
        self.moveRight = True
        self.lastMoveLeft = False
        self.index = 0

        if platform != None:
            self.y = platform.rect.y + 2
            self.jumpGround = platform.rect.y + 2

    def goClimbUp(self, Ladder = None):
        self.y -= constants.HERO_CLIMB_SPEED
        self.onLadder = True
        self.doClimbing = True
        self.climbingUp  = True
        self.index = 0
        if Ladder is not None:
            self.rect.centerx = Ladder.rect.centerx
            self.x = self.rect.x

    def goClimbDown(self, Ladder = None):
        self.y += constants.HERO_CLIMB_SPEED
        self.onLadder = True
        self.doClimbing = True
        self.climbingUp = False
        self.index = 0

    def doStopClimbing(self):
        self.doClimbing = False

    def doStopRunning(self):
        self.index = 0
        self.stopping = 140
        self.moveLeft = self.moveRight = False

    def doActionOne(self, ground_y):
        # print(self.rect.bottom, ground_y, self.y)
        self.onLadder = False
        self.doClimbing = True
        if self.rect.bottom == ground_y:
            self.jumpMove = -constants.ERIK_JUMP_FORCE
            self.jumpGround = ground_y
            self.stopping = -1
            self.running_time = 0

    def render_jumping(self):
        self.image = self.sprite_jumping.next(self.lastMoveLeft) 

    def render_climbing(self):
        if self.doClimbing:
            if self.climbingUp:
                self.image = self.sprite_climbing.next()
            else:
                self.image = self.sprite_climbing.prev()
        else:
            self.image = self.sprite_climbing.curr()

    def render_standing(self):
        if self.jumpMove <= constants.ERIK_JUMP_FORCE:
            self.render_jumping()
            self.index = 0
        else:
            self.index += 1
            self.index %= constants.ERIK_STAND_TYING_TIME      

            if self.index > constants.ERIK_STAND_TYING_TIME - constants.ERIK_STAND_TYING_DELAY:
                self.image = self.sprite_tying.next(self.lastMoveLeft)
            else:
                self.image = self.sprite_stand.next(self.lastMoveLeft)

    def render_running(self):
        self.index += 1
        self.index %= self.running_interval

        if self.jumpMove <= constants.ERIK_JUMP_FORCE:
            self.render_jumping()
        else:
            self.image = self.sprite_running.next(self.moveLeft)

    def render_stoping(self):
        self.stopping -= 1  # -1, 0..140
        if self.stopping < 0:
            self.running_time = 0

        self.image = self.sprite_stoping.next(self.lastMoveLeft)

    def update(self, platform = None):
        self.isFalling()
        if self.onLadder:
            if self.doClimbing:
                if self.climbingUp:
                    self.y -= constants.HERO_CLIMB_SPEED
                else:
                    self.y += constants.HERO_CLIMB_SPEED
            self.render_climbing()
        else:
            # calc jumping mechanics
            if self.jumpMove <= constants.ERIK_JUMP_FORCE:
                if self.y + self.jumpMove < self.jumpGround:
                    self.y += self.jumpMove
                    if self.jumpMove < constants.ERIK_JUMP_FORCE:
                        self.jumpMove += 1
                else:
                    self.y = self.jumpGround
                    self.jumpMove = constants.ERIK_JUMP_FORCE + 1
                    self.sprite_jumping.reset()

            # if standing
            if not (self.moveLeft or self.moveRight):
                if self.stopping >= 0 and self.running_time > 40:
                    self.render_stoping()
                else:
                    self.render_standing()
                    self.running_time = 0

            else:  # if running
                if self.moveLeft:
                    self.x -= constants.ERIK_WALK_SPEED
                else:
                    self.x += constants.ERIK_WALK_SPEED
                self.render_running()
                self.running_time += 1

        self.rect.x = self.x
        # self.rect.y = self.y
        self.rect.bottom = self.y
