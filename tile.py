import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.tile_image = pygame.image.load("Graphics/p1/tile.png").convert_alpha()
        self.image = self.tile_image
        self.rect = self.image.get_rect(topleft=pos)
