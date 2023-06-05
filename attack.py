import pygame
from settings import scrn_w
class Attack(pygame.sprite.Sprite):

    def __init__(self, pos, direction, p_num, spr_bullet, spr_bullet_reverse):
        super().__init__()
        self.spr_bullet = spr_bullet
        self.spr_bullet_reverse = spr_bullet_reverse
        self.image = pygame.Surface((30, 10))
        self.rect = self.image.get_rect(topleft=pos)
        if p_num == 1:
            self.speed = 10
        if p_num == 2:
            self.speed = 8

        self.image = pygame.image.load(self.spr_bullet)

        if direction == 0 and p_num == 1:
            direction = 1
            self.image = pygame.image.load(self.spr_bullet_reverse)
        if direction == 0 and p_num == 2:
            direction = -1
            self.image = pygame.image.load(self.spr_bullet)
        self.direction = pygame.math.Vector2(direction * self.speed, 0)
        if self.direction.x < 0:
            self.image = pygame.image.load(self.spr_bullet)
        if self.direction.x > 0:
            self.image = pygame.image.load(self.spr_bullet_reverse)

    def update(self):
        self.rect.x += self.direction.x
        if self.rect.x > scrn_w or self.rect.x < 0:
            self.kill()
        if self.rect.x > self.rect.x + 2 or self.rect.x < self.rect.x - 2:
            self.kill()

#

