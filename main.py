import pygame
import pause
import settings
import player
import source
import pipes
import ground
import pygame.freetype

pygame.init()


class Game:
    def __init__(self):
        self.value_for_while = True
        self.fp = 0
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode(settings.SIZE)
        pygame.display.set_caption('Flappy Bird')
        self.player = player.Bird(self)
        self.back = source.back
        self.pipes = []
        self.space = 300
        self.condition = 'game'
        self.lose = source.lose
        self.lose_size = self.lose.get_size()
        self.pause = source.pause
        self.pause_size = self.pause.get_size()
        self.x_lose = settings.WIDTH // 2 - self.lose_size[0] // 2
        self.y_lose = settings.HEIGHT // 2 - self.lose_size[1] // 2
        self.score = 1
        self.level = 1
        self.font = pygame.freetype.Font(None, 30)
        self.start_value = False
        self.button = pause.Pb(self)
        self.ground = ground.Ground(self)
        self.fp_mousedown = 0
        self.fp_for_down = 0

    def events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.value_for_while = False
            if event.type == pygame.MOUSEBUTTONDOWN and self.condition != 'falling':
                self.start_value = True
                self.player.hitbox.y -= 50
                self.player.speed_fall = 0
                self.fp_mousedown = self.fp
                self.fp_for_down = 0
                self.player.animation_list = self.player.sprites_up
                if self.button.hitbox.collidepoint(event.pos) and self.condition != 'lose':
                    self.condition = 'pause'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.condition == 'lose':
                        self.replay()
                    if self.condition == 'pause':
                        self.condition = 'game'

    def draw(self):
        self.window.blit(self.back, [0, 0])
        if self.start_value == True:
            if self.fp % 250 == 0:
                self.pipe = pipes.Pipes(self)
                self.pipes.append(self.pipe)

            for pipe in self.pipes:
                pipe.draw()
                pipe.update()
                if pipe.hitbox1.right < 0:
                    self.pipes.remove(pipe)
                if pipe.hitbox1.right < self.player.hitbox.left and pipe.ready == False:
                    self.score += 1
                    pipe.ready = True

        self.player.draw()
        self.button.draw()
        self.ground.draw()

    def update(self):
        if self.start_value == True:
            self.player.update()
        for pipe in self.pipes:
            pipe.update()
            if self.player.hitbox.colliderect(pipe.hitbox1) == True or self.player.hitbox.colliderect(
                    pipe.hitbox2) == True:
                self.condition = 'falling'
        if self.score % 50 == 0 and self.space >= 50 and self.score % 50 == self.level - 1:
            self.space -= 10
            self.level += 1
        if self.player.hitbox.colliderect(self.ground.hitbox1) == True or self.player.hitbox.colliderect(
                self.ground.hitbox2) == True:
            self.condition = 'lose'
        self.ground.update()

        if self.fp_mousedown + 20 == self.fp:
            self.player.animation_list = self.player.sprites
            self.fp_for_down = self.fp
        if self.fp_for_down + 20 == self.fp and self.start_value == True:
            self.player.animation_list = self.player.sprites_down
        self.player.animate()
        print(self.player.animation)

    def text(self):
        self.font.render_to(self.window, [500, 285], f'{self.score - 1}', [240, 17, 17])
        self.font.render_to(self.window, [500, 370], f'{self.level}', [20, 17, 240])

    def replay(self):
        self.condition = 'game'
        self.score = 1
        self.level = 1
        self.pipes = []
        self.player.hitbox.x = settings.WIDTH // 4
        self.player.hitbox.y = settings.HEIGHT // 2
        self.start_value = False
        self.player.animation_list = self.player.sprites

    def pause_func(self):
        self.window.blit(self.pause, [self.x_lose, self.y_lose])
        self.events()
        self.text()

    def fall_down(self):
        self.player.animation_list = self.player.sprites_fall_down
        self.player.animation = -1
        self.player.fall_down_update()
        if self.player.hitbox.colliderect(self.ground.hitbox1) or self.player.hitbox.colliderect(self.ground.hitbox2):
            self.condition = 'lose'

    def start(self):
        while self.value_for_while == True:
            if self.condition == 'game':
                self.draw()
                self.events()
                self.update()
            elif self.condition == 'lose':
                self.window.blit(self.lose, [self.x_lose, self.y_lose])
                self.events()
                self.text()
            elif self.condition == 'falling':
                self.fall_down()
                self.draw()
                self.events()
            elif self.condition == 'pause':
                self.pause_func()
            pygame.display.update()
            self.fp += 1
            self.clock.tick(100)


game = Game()
game.start()
