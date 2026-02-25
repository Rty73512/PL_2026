import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))

# заливка фона
screen.fill((255, 255, 255))
pygame.display.flip()

# основание
circle(screen, (0, 0, 0), (250, 250), 202)
circle(screen, (255, 255, 0), (250, 250), 200)

# рот
rect(screen, (0, 0, 0), (150, 350, 200, 50))

# глаза
circle(screen, (0, 0, 0), (175, 200), 32)
circle(screen, (255, 0, 0), (175, 200), 30)
circle(screen, (0, 0, 0), (175, 200), 15)

circle(screen, (0, 0, 0), (325, 200), 27)
circle(screen, (255, 0, 0), (325, 200), 25)
circle(screen, (0, 0, 0), (325, 200), 10)

# брови
pygame.draw.line(screen, (0, 0, 0), (110, 110), (200, 175), 15)  
pygame.draw.line(screen, (0, 0, 0), (300, 175), (400, 130), 15)  

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    



pygame.quit()