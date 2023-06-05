import pygame

from settings import tile_size
from tile import Tile
from player import *
from star import *
import time
#time is needed to regenerate the stars every 30 seconds outside of the update function in player.py
class Level:
    def __init__(self, level_data, surface):

        self.display_surface = surface
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        self.star = pygame.sprite.Group()
        self.level_data = level_data
        self.setup_level(level_data)

        self.star_timer = time.time()
        #self.screen = screen

        #MUSIC IS HERE

        #pygame.mixer.music.load("music/doffy.mp3")
        pygame.mixer.music.load("music/zoro.mp3")
        pygame.mixer.music.play(-1)
        #plays music on repeat from a downloaded mp3
    def setup_level(self, layout):

        for row_index, row in enumerate(layout):
            for cell_index, cell in enumerate(row):
                x = cell_index * tile_size
                y = row_index * tile_size
                if cell == "x":
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                elif cell == "s":
                    star = Star((x,y))
                    self.star.add(star)
                elif cell == "q": #right side PLAYER 2
                    player_sprite2 = Player((x,y), 2, "blue", "Graphics/p3/SANJISTANDJ.png", "Graphics/p3/SANJIWALKF.png", "Graphics/p3/SANJIJUMPF.png", "Graphics/p3/SANJIWALKREVERSEF.png", "Graphics/p3/SANJIJUMPREVERSEF.png", "Graphics/p3/SANJIDASH.png", "Graphics/p3/SANJIDASHREVERSE.png", "Graphics/p3/SANJIATTACK.png", "Graphics/p3/SANJIATTACKREVERSE.png", "Graphics/p3/SANJIDEAD.png",  "Graphics/p3/SANJIBULLET.png",  "Graphics/p3/SANJIBULLETREVERSE.png", "Graphics/p3/SANJICHARGE.png")
                    self.player.add(player_sprite2)
                elif cell == "p": #left side PLAYER 1
                    player_sprite1 = Player((x,y), 1, "red", "Graphics/p1/LUFFYSTANDF.png", "Graphics/p1/LUFFYRUNF.png", "Graphics/p1/LUFFYJUMPF.png", "Graphics/p1/LUFFYRUNFLIPF.png", "Graphics/p1/LUFFYJUMPREVERSEF.png", "Graphics/p1/LUFFYDASH.png", "Graphics/p1/LUFFYDASHREVERSE.png", "Graphics/p1/LUFFYATTACK.png", "Graphics/p1/LUFFYATTACKREVERSE.png", "Graphics/p1/LUFFYDEAD.png",  "Graphics/p1/LUFFYBULLET.png",  "Graphics/p1/LUFFYBULLETREVERSE.png", "Graphics/p1/LUFFYCHARGEREVERSE.png")
                    self.player.add(player_sprite1)

            #adds stars tile and players
            #seperation between the players with all their individual characteristics/variables given here,
            #including the p_num (1,2) which identifies the different players
    def run(self):
        self.tiles.draw(self.display_surface)
        self.player.update(self.tiles)
        self.player.draw(self.display_surface)
        self.star.draw(self.display_surface)



        for p in self.player:
            p.draw_attacks(self.display_surface)
            coll = pygame.sprite.groupcollide(self.player,p.attacks, False, False)
            wall = pygame.sprite.groupcollide(self.tiles,p.attacks, False, True)
            for c in coll:
                if c != p:
                    c.playerhealth -= 10
        for s in self.star:
            collide = pygame.sprite.groupcollide(self.player, self.star, False, True)
            for c in collide:
                c.playerhealth += 200

            #records the collisions
            #if collision is with player it does 10 damage
            #if collision is with wall it destroys the bullet line 58

        if time.time() - self.star_timer >= 30:
            for row_index, row in enumerate(self.level_data):
                for cell_index, cell in enumerate(row):
                    x = cell_index * tile_size
                    y = row_index * tile_size
                    if cell == "s":
                        star = Star((x,y))
                        self.star.add(star)
            self.star.draw(self.display_surface)
            self.star_timer = time.time()


            #simply redoes the entire screen, regenerating the stars every 30 seconds

