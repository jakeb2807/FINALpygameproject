import pygame
class Star(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.star_sprite = pygame.image.load("Graphics/p1/star.png")
        self.image = self.star_sprite
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect(topleft=pos)



