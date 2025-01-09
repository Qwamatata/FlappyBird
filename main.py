import pygame
import settings

class Game:
    def __init__(self):
        self.value_for_while = True
        self.fp = 0
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode(settings.SIZE)
        pygame.display.set_caption('Flappy Bird')

    def events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.value_for_while = False

    def draw(self):
        pass

    def update(self):
        pass

    def start(self):
        while self.value_for_while == True:
            self.draw()
            self.events()
            self.update()
            pygame.display.update()
            self.fp += 1
            self.clock.tick(100)

game = Game()
game.start()