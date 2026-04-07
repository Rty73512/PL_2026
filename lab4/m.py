import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 2
screen = pygame.display.set_mode((1000, 1000))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


position = [[0, 0, 0, (0, 0, 0)]*10 ]
score = 0
level = 0

def new_ball(position):
    '''создает новый шарик '''
    for x in range(len(position)):
        if position[x] == [0, 0, 0, (0, 0, 0)]:
            x = randint(100, 1100)
            y = randint(100, 900)
            r = randint(10, 100)
            color = COLORS[randint(0, 5)]
            position[x] = [x, y, r, color]
    return position

def draw_ball(position, level):
    '''рисует шарик'''
    for x in range(level+2):
        circle(screen, position[x][3], (position[x][0], position[x][1]), position[x][2])


def hit(event , position):
    '''проверяет попадание'''
    hit = event.pos
    for x in range(len(position)):
        if ((position[x][0]-position[x][2])<=hit[0]<=(position[x][0]+position[x][2])) and ((position[x][1]-position[x][2])<=hit[1]<=(position[x][1]+position[x][2])):
            return 1
        else:
            return 0

def draw(score, level):
    '''отрисовка счета и уровня'''
    font = pygame.font.Font(None, 36) 
    text_surface = font.render(f"Счёт: {score}", True, (255, 255, 255))
    screen.blit(text_surface, (10, 10))

def move(position, n):
    """Перемещает шарик и обрабатывает отскоки от стен"""
    while True:
        vx = randint(-5, 5)
        vy = randint(-5, 5)
        position[n][0] += vx
        position[n][1] += vy
        if position[n][0] <= 0 or position[n][0] >= 1000:
            position[n][0] -= vx
            continue
        if position[n][1] <= 0 or position[n][1] >= 1000:
            position[n][1] -= vx
            continue
        break

print(position)
position = new_ball(position)
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if hit(event, position) == 1:
                score +=10
    
    
    print(position)
    draw_ball(position, level)
    print(position)
    draw(score, level)
    move(position, level)
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()