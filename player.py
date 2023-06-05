import pygame
from settings import gravity
from attack import Attack
from settings import scrn_w, scrn_h
from level import *
from star import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, p_num, colour, spr_idle, spr_run, spr_jump, spr_run_reverse, spr_jump_reverse, spr_dash, spr_dash_reverse, spr_attack, spr_attack_reverse, spr_dead, spr_bullet, spr_bullet_reverse, spr_charge): #ADD VARIABLES HERE
        super().__init__()
        #self.image = pygame.Surface((32,64))
        #self.image.fill(colour)
        self.direction = pygame.math.Vector2(0,0)
        self.image = pygame.image.load(spr_idle)


        #I TOOK OUT THEIR VARIABLE IN THE PLAYWER
        #self.loc = loc
        #self.colourt = colourt



        #self.screen = screen #NO SCREEN VARIABLE IN PLAYER ABOVE

#ADD VARIABLE FOR LUFFY CHARGE JUMP WITH NEW SPRITE FOR IT MAKE IT SO THAT FOR EVERY 1 S holding down Key down arrow the variable
        #self.luffycharge += 1 and its a multiplyers for jump strength
        self.luffycharge = 0.75
        self.chargecount = 0


        #sprites
        self.spr_charge = spr_charge
        self.spr_bullet = spr_bullet
        self.spr_bullet_reverse = spr_bullet_reverse
        self.spr_idle = spr_idle
        self.spr_run = spr_run
        self.spr_jump = spr_jump
        self.spr_jump_reverse = spr_jump_reverse
        self.spr_run_reverse = spr_run_reverse
        self.spr_dash = spr_dash
        self.spr_dash_reverse = spr_dash_reverse
        self.spr_attack = spr_attack
        self.spr_attack_reverse = spr_attack_reverse
        self.spr_dead = spr_dead


        self.rect = self.image.get_rect(topleft=pos)

        self.speed = 0 #adjusted per player below
        self.jump_speed = 0 #dash speed changed in keys since it seperates players


        self.status = "yes"
        self.dash = "yes"
        self.dashsprite = "no"


        self.attacks = pygame.sprite.Group()  #BULLET GROUP
        self.star = pygame.sprite.Group()



        self.firing = False
        self.count = 0
        self.dashcounter = 0
        self.doublejump = 0
        self.shotcheck = "yes"
        self.shotclock = 0
        self.attackcheck = "yes"
        self.attackcount = 0
        self.headcount = 0
        self.headhit = "no"
        self.p_num = p_num
        self.timer = 0
        self.shotclock2 = 0
        self.shotsprite = ""
        self.deathtimer = 0
        self.deathsprite = ""
        self.a = ""
        self.b = 0


        if self.p_num == 2:
            self.playerhealth = 450
            self.heart_x = 50
            self.heart_y = -50
        if self.p_num == 1:
            self.playerhealth = 500
            self.heart_x = 20
            self.heart_y = -20


        self.full_heart = pygame.image.load("Graphics/p1/fullheart.png")
        self.half_heart = pygame.image.load("Graphics/p1/halfheart.png")
        self.empty_heart = pygame.image.load("Graphics/p1/emptyheart.png")
        self.playerper = ""


        #self.screen.blit(self.heart_image, (self.heart_x, self.heart_y))


    def get_input(self):
        keys = pygame.key.get_pressed()
#player 1
        self.direction.x = 0
        if keys[pygame.K_RIGHT] and self.p_num == 2 and self.a != "yes":
            self.direction.x = 1
        if keys[pygame.K_LEFT] and self.p_num == 2 and self.a != "yes":
            self.direction.x = -1
        if keys[pygame.K_UP] and self.headhit == "no" and self.p_num == 2 and self.a != "yes":
            self.jump()
        if keys[pygame.K_LEFT] and keys[pygame.K_DOWN] and self.p_num == 2 and self.a != "yes":
            if self.dash == "yes":
                self.direction.x = -35
                self.dash = "no"
                self.dashsprite = "yes"
        if keys[pygame.K_DOWN] and keys[pygame.K_RIGHT] and self.p_num == 2 and self.a != "yes":
            if self.dash == "yes":
                self.direction.x = 35
                self.dash = "no"
                self.dashsprite = "yes"

        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and self.p_num == 2 and self.a != "yes":
            self.direction.x = 0

        if keys[pygame.K_BACKSPACE] and not self.firing and self.p_num == 2 and self.a != "yes":
            self.fire()
            self.firing = True
            self.shotsprite = "yes"
        elif not keys[pygame.K_BACKSPACE] and self.firing and self.shotcheck == "yes" and self.a != "yes":
            self.firing = False
#player 2
        if keys[pygame.K_d] and self.p_num == 1 and self.a != "yes":
            self.direction.x = 1
        if keys[pygame.K_a] and self.p_num == 1 and self.a != "yes":
            self.direction.x = -1
        if keys[pygame.K_w] and self.headhit == "no" and self.p_num == 1 and self.a != "yes":
            self.jump()
        if keys[pygame.K_a] and keys[pygame.K_s] and self.p_num == 1 and self.a != "yes":
            if self.dash == "yes":
                self.direction.x = -25
                self.dash = "no"
                self.dashsprite = "yes"
        if keys[pygame.K_s] and keys[pygame.K_d] and self.p_num == 1 and self.a != "yes":
            if self.dash == "yes":
                self.direction.x = 25
                self.dash = "no"
                self.dashsprite = "yes"

        if keys[pygame.K_a] and keys[pygame.K_d] and self.p_num == 1 and self.a != "yes":
            self.direction.x = 0
        if keys[pygame.K_SPACE] and not self.firing and self.p_num == 1 and self.a != "yes":
            self.fire()
            self.firing = True
            self.shotsprite = "yes"
        elif not keys[pygame.K_SPACE] and self.firing and self.shotcheck == "yes" and self.a != "yes":
            self.firing = False
    def fire(self):
        attack1 = Attack((self.rect.centerx, self.rect.centery), self.direction.x, self.p_num, self.spr_bullet, self.spr_bullet_reverse)
        self.attacks.add(attack1)
        self.shotcheck = "no"
        self.attackcheck = "no"


    def jump(self):
        if self.status == "yes" and self.doublejump != 2 and self.p_num == 2:
            self.status = "no"
            self.direction.y = self.jump_speed
            if self.p_num == 2:
                self.doublejump += 1
            if self.p_num == 1:
                self.doublejump += 2

        if self.status == "yes" and self.doublejump != 2 and self.p_num == 1:
            self.status = "no"
            self.direction.y = self.jump_speed * self.luffycharge
            if self.p_num == 2:
                self.doublejump += 1
            if self.p_num == 1:
                self.doublejump += 2
            self.luffycharge = 0.75


    def hor_mov_collision(self, tiles):
        self.rect.x += self.direction.x * self.speed

        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect):   #the direction references is the direction the p is going when collide
                if self.direction.x > 0:  #right
                    self.rect.right = tile.rect.left
                    self.doublejump = 0
                if self.direction.x < 0:  #left
                   self.rect.left = tile.rect.right
                   self.doublejump = 0
    def ver_mov_collision(self, tiles):
        self.apply_gravity()



        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect):
                if self.direction.y > 0: #down
                    self.rect.bottom = tile.rect.top
                    self.direction.y = 0
                    self.count = 0
                    self.status = "yes"
                    self.headhit = "no"
                    self.doublejump = 0
                if self.direction.y < 0: #top
                    self.rect.top = tile.rect.bottom
                    self.headhit = "yes"
    def apply_gravity(self):
        self.direction.y += gravity
        self.rect.y += self.direction.y




    def update(self, tiles):
        keys = pygame.key.get_pressed()
        self.get_input()
        self.hor_mov_collision(tiles)
        self.ver_mov_collision(tiles)
        self.attacks.update()

        ######### self.stars.update() ????





        if self.status == "no":
            self.count += 1
            if self.count > 15:
                self.status = "yes"
                self.count = 0
        if self.dash == "no":
            self.dashcounter += 1
            if self.dashcounter > 30:
                self.dashsprite = "no"
            if self.dashcounter > 120 and self.p_num == 2:
                self.dash = "yes"
                self.dashcounter = 0
                self.dashsprite = "yes"
            if self.dashcounter > 150 and self.p_num == 1:
                self.dash = "yes"
                self.dashcounter = 0
                self.dashsprite = "yes"
        if self.rect.x > scrn_w + 5 or self.rect.x < -20 or self.rect.y > scrn_h + 5:
            self.playerhealth = 0
        if self.playerhealth <= 0:
            self.a = "yes"
            self.deathsprite = "yes"

        if self.a == "yes":
            self.b += 1
            self.playerhealth = 0
            self.playerper = 0
            if self.b > 60:
                print("Player " + str(self.p_num) + " died")
                exit()
        if self.shotcheck == "no":
            self.shotclock += 1
            self.shotclock2 += 1
            if self.shotclock > 20:
                self.shotcheck = "yes"
                self.shotclock = 0
            if self.shotclock2 > 30:
                self.shotsprite = "no"
                self.shotclock2 = 0
        if self.attackcheck == "no":
            self.attackcount += 1 #KILLS BULLETS AFTER SHOT DOESNT WORK
            if self.attackcount > 20:
                self.attackcheck = "yes"
                self.attackcount = 0

        if self.headhit == "yes":
            self.headcount += 1
            if self.headcount > 60:
                self.headhit = "no"
                self.headcount = 0
        if self.direction.x == 0 and self.direction.y == 0 and self.deathsprite != "yes":
            self.image = pygame.image.load(self.spr_idle)
        elif self.direction.x < 0 and self.direction.y == 0 and self.deathsprite != "yes":  #left
            self.image = pygame.image.load(self.spr_run)
        elif self.direction.x > 0 and self.direction.y == 0 and self.deathsprite != "yes": #right
            self.image = pygame.image.load(self.spr_run_reverse)
        elif self.direction.y < 0 and self.deathsprite != "yes":
            if self.direction.x <= 0:
                self.image = pygame.image.load(self.spr_jump)
            elif self.direction.x > 0:
                self.image = pygame.image.load(self.spr_jump_reverse)



        if keys[pygame.K_LEFT] and keys[pygame.K_DOWN] and self.p_num == 2 and self.dashsprite == "yes" and self.deathsprite != "yes":
            self.image = pygame.image.load(self.spr_dash)
        if keys[pygame.K_DOWN] and keys[pygame.K_RIGHT] and self.p_num == 2 and self.dashsprite == "yes" and self.deathsprite != "yes":
            self.image = pygame.image.load(self.spr_dash_reverse)


        if keys[pygame.K_a] and keys[pygame.K_s] and self.p_num == 1 and self.dashsprite == "yes" and self.deathsprite != "yes":
            self.image = pygame.image.load(self.spr_dash)
        if keys[pygame.K_s] and keys[pygame.K_d] and self.p_num == 1 and self.dashsprite == "yes" and self.deathsprite != "yes":
            self.image = pygame.image.load(self.spr_dash_reverse)

        if keys[pygame.K_BACKSPACE] and self.p_num == 2 and self.shotsprite == "yes" and self.deathsprite != "yes":
            if self.direction.x <= 0: #left sanji
                self.image = pygame.image.load(self.spr_attack)
            if self.direction.x > 0:
                self.image = pygame.image.load(self.spr_attack_reverse)
        if keys[pygame.K_SPACE] and self.p_num == 1 and self.shotsprite == "yes" and self.deathsprite != "yes":
            if self.direction.x < 0: #left luffy
                self.image = pygame.image.load(self.spr_attack)
            if self.direction.x >= 0:
                self.image = pygame.image.load(self.spr_attack_reverse)

        #shooting sprite depending on the direction of movement


        if self.deathsprite == "yes":
            self.image = pygame.image.load(self.spr_dead)

        if self.p_num == 1: #luffy
            self.jump_speed = -22
            self.speed = 5
        if self.p_num == 2: #sanji
            self.jump_speed = -17
            #give sanji and bigger one jump without charge but half of max charge luffyjump
            self.speed = 6


        if keys[pygame.K_v] and self.direction.y == 0 and self.p_num == 1:
            if self.direction.x == 0:
                self.image = pygame.image.load(self.spr_charge)
            self.chargecount += 1
            if self.chargecount > 1.75:
                self.luffycharge += 0.04
                self.chargecount = 0
        if self.luffycharge > 1.6:
            self.luffycharge = 1.6
        if self.direction.x != 0:
            self.luffycharge = 0.75

        #this work to build up the charge of the player 1
        #when the v button is held while the player isnt moving it begins increasing the charge count
        #for every time the chargecount gets above 1.75 it directly adds to the luffycharge, which is a multiplyer to jump strength
        #however it has a cap at 1.6 to ensure the jump doesn't go to high
        #and if they move the jump is reverted to the base 0.75


        if self.p_num == 1:
            if self.playerhealth > 500:
                self.playerhealth = 500
            self.playerper = self.playerhealth/500*100
        elif self.p_num == 2:
            if self.playerhealth > 250:
                self.playerhealth = 250
            self.playerper = self.playerhealth/250*100

        if self.playerper >= 75:
            self.heart_image = self.full_heart
        elif self.playerper >= 25:
            self.heart_image = self.half_heart
        else:
            self.heart_image = self.empty_heart

##########################

    #work on building the power up attack system after the system for health stars


    def draw_attacks(self, surface):
        self.attacks.draw(surface)


