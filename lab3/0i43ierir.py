import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

# Цвета
GRAY = (180, 180, 180)
DARK_GRAY = (130, 130, 130)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 192, 203)
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)

def crt(screen, x, y, size):
    polygon(screen, ORANGE, [(x, y), (x+30*size, y), (x+15*size, y+size*40)])
    line(screen, GREEN, (x+15*size, y), (x+15*size, y-10*size))
    line(screen, GREEN, (x+15*size, y), (x+20*size, y-10*size))
    line(screen, GREEN, (x+15*size, y), (x, y-10*size))

crt(screen, 30,30, 3)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()