import pygame
import settings

bird = pygame.image.load('Flappy Bird Assets/Player/StyleBird1/Bird1-4.png')
bird = pygame.transform.scale(bird, [settings.SIZE_FOR_BIRD * 4, settings.SIZE_FOR_BIRD])

back = pygame.image.load('Flappy Bird Assets/Background/Background5.png')
back = pygame.transform.scale(back, settings.SIZE)

pipes_initial = pygame.image.load('Flappy Bird Assets/Tiles/Style 1/PipeStyle1.png')
pipes_initial_size = pipes_initial.get_size()
part_width = pipes_initial_size[0] // 4
part_height = pipes_initial_size[1] // 2
pipe = pipes_initial.subsurface(pygame.Rect(0, 0, part_width, part_height))

lose = pygame.image.load('lose.png')
lose = pygame.transform.scale(lose, [450,300])

pause = pygame.image.load('pause.png')
pause = pygame.transform.scale(pause,[450,300])

pause_but = pygame.image.load('Flappy Bird Assets/pause_button.png')
pause_but = pygame.transform.scale(pause_but,[50,50])

ground = pygame.image.load('Flappy Bird Assets/ground.png')
ground = pygame.transform.scale(ground,[settings.WIDTH + 100,30])