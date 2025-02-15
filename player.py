import pygame
import settings
import source


class Bird:
    def __init__(self, game):
        self.image = source.bird
        self.game = game
        width, height = self.image.get_size()
        part_width = width // 4
        part_height = height
        self.sprites = []
        self.sprites_up = []
        self.sprites_fall_down = []
        self.sprites_down = []
        for i in range(4):
            x = i * part_width
            sprite = self.image.subsurface(pygame.Rect(x, 0, part_width, part_height))
            self.sprites.append(sprite)

        for i in range(30, 46, 5):
            for sprite in self.sprites:
                sprite_up = pygame.transform.rotate(sprite, i)
                self.sprites_up.append(sprite_up)
        for sprite in self.sprites:
            sprite_fall_down = pygame.transform.rotate(sprite, -90)
            self.sprites_fall_down.append(sprite_fall_down)

        for i in range(-84, -45):
            for sprite in self.sprites:
                sprite_down = pygame.transform.rotate(sprite, i)
                self.sprites_down.append(sprite_down)

        sizes = self.sprites[0].get_size()
        self.hitbox = pygame.Rect([settings.WIDTH // 4, settings.HEIGHT // 2], sizes)
        self.speed_fall = 1
        self.animation = 0
        self.animation_list = self.sprites

    def draw(self):
        self.game.window.blit(self.animation_list[self.animation], self.hitbox)

    def update(self):
        self.speed_fall += 0.1
        self.hitbox.y += self.speed_fall


    def fall_down_update(self):
        self.speed_fall += 0.5
        self.hitbox.y += self.speed_fall

    def animate(self):
        if self.game.fp % 15 == 0:
            if self.animation < len(self.animation_list) - 1:
                self.animation += 1
            else:
                self.animation = 0
        if self.animation > len(self.animation_list) - 1:
            self.animation = 0
