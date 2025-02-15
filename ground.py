import pygame
import source
import settings


class Ground:
    def __init__(self, game):
        self.game = game
        self.picture = source.ground
        self.sizes = self.picture.get_size()
        self.speed = 2
        self.hitbox1 = pygame.Rect([0, settings.HEIGHT - self.sizes[1]], self.sizes)
        self.hitbox2 = pygame.Rect([settings.WIDTH + 10, settings.HEIGHT - self.sizes[1]], self.sizes)

    def draw(self):
        self.game.window.blit(self.picture, self.hitbox1)
        self.game.window.blit(self.picture, self.hitbox2)

    def update(self):
        self.hitbox1.x -= self.speed
        self.hitbox2.x -= self.speed
        if self.hitbox1.right < 0:
            self.hitbox1.x = settings.WIDTH
        if self.hitbox2.right < 0:
            self.hitbox2.x = settings.WIDTH + 10
