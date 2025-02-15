import pygame
import source

class Pb:
    def __init__(self,game):
        self.game = game
        self.picture = source.pause_but
        self.hitbox = pygame.Rect([0,0],self.picture.get_size())

    def draw(self):
        self.game.window.blit(self.picture,self.hitbox)

