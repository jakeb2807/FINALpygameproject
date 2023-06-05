import pygame, sys
from settings import *
from level import Level

pygame.init()
screen = pygame.display.set_mode((scrn_w, scrn_h))
clock = pygame.time.Clock()
level = Level(level_map, screen)
bg_image = pygame.image.load("Graphics/p1/Oni.png")
#Backgroudn image


#font = pygame.font.Font("Graphics/p1/FreeSansBold.ttf")
#text = font.render("Health: " + str(level.player.sprite.playerper), True, level.player.sprite.colourt)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(bg_image, (0, 0))
    level.run()
    pygame.display.update()
    clock.tick(fps)


    #font = pygame.font.Font("Graphics/p1/FreeSansBold.ttf")
    #text = font.render("Health: " + str(level.player.sprite.playerper), True, level.player.sprite.colourt, level.player.sprite.loc)
    #screen.blit(text, level.player.sprite.loc)










#Kids




