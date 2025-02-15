import pygame
import source
import random
import settings


class Pipes:
    def __init__(self, game):
        self.game = game
        picture = source.pipe
        width = 100
        height = random.randint(100, 275)
        size1 = [width, height]
        size2 = [width, settings.HEIGHT - size1[1] - self.game.space]
        self.picture1 = pygame.transform.scale(picture, size1)
        self.picture2 = pygame.transform.scale(picture, size2)
        self.hitbox1 = pygame.Rect(settings.WIDTH, 0, size1[0], size1[1])
        self.hitbox2 = pygame.Rect(settings.WIDTH, settings.HEIGHT - size2[1], size2[0], size2[1])
        self.speed = 1
        self.ready = False
        self.hitbox2.y -= self.game.ground.sizes[1]

    def draw(self):
        self.game.window.blit(self.picture1, self.hitbox1)
        self.game.window.blit(self.picture2, self.hitbox2)

    def update(self):
        self.hitbox1.x -= self.speed
        self.hitbox2.x -= self.speed
