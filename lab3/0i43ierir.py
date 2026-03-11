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

# Координаты центра и размеры зайца
x, y = 200, 200
width, height = 200, 400

# Рисуем тело
body_width = width // 2
body_height = height // 2
body_y = y + body_height // 2
ellipse(screen, GRAY, (x - body_width // 2, body_y - body_height // 2, body_width, body_height))

# Рисуем уши с контуром
head_size = height // 4
ear_height = height // 3
ear_y = y - height // 2 + ear_height // 2
ear_width = width // 8

# Левое ухо
ear_x = x - head_size // 4
ellipse(screen, GRAY, (ear_x - ear_width // 2, ear_y - ear_height // 2, ear_width, ear_height))
ellipse(screen, DARK_GRAY, (ear_x - ear_width // 2, ear_y - ear_height // 2, ear_width, ear_height), 2)
ellipse(screen, PINK, (ear_x - ear_width // 4, ear_y - ear_height // 4, ear_width//2, ear_height//2))

# Правое ухо
ear_x = x + head_size // 4
ellipse(screen, GRAY, (ear_x - ear_width // 2, ear_y - ear_height // 2, ear_width, ear_height))
ellipse(screen, DARK_GRAY, (ear_x - ear_width // 2, ear_y - ear_height // 2, ear_width, ear_height), 2)
ellipse(screen, PINK, (ear_x - ear_width // 4, ear_y - ear_height // 4, ear_width//2, ear_height//2))


# Рисуем голову
head_y = y - head_size // 2
circle(screen, GRAY, (x, head_y), head_size // 2)

# Рисуем глаза
eye_size = head_size // 3
eye_y = head_y - 5
eye_offset = head_size // 4

# Левый глаз
eye_x = x - eye_offset
circle(screen, WHITE, (eye_x, eye_y), eye_size // 2) 
circle(screen, BLACK, (eye_x, eye_y), eye_size // 4)  
circle(screen, WHITE, (eye_x - 2, eye_y - 2), 2)      

# Правый глаз
eye_x = x + eye_offset
circle(screen, WHITE, (eye_x, eye_y), eye_size // 2) 
circle(screen, BLACK, (eye_x, eye_y), eye_size // 4)  
circle(screen, WHITE, (eye_x - 2, eye_y - 2), 2)      

# Рисуем нос
nose_y = head_y + 10
circle(screen, BLACK, (x, nose_y), 3)

# Рисуем рот
line(screen, BLACK, (x, nose_y + 3), (x - 5, nose_y + 10), 2)
line(screen, BLACK, (x, nose_y + 3), (x + 5, nose_y + 10), 2)

# Рисуем ноги
leg_height = height // 16
leg_y = y + height // 2 - leg_height // 2

# Левая нога
leg_x = x - width // 4
ellipse(screen, GRAY, (leg_x - (width // 4) // 2, leg_y - leg_height // 2, width // 4, leg_height))

# Правая нога
leg_x = x + width // 4
ellipse(screen, GRAY, (leg_x - (width // 4) // 2, leg_y - leg_height // 2, width // 4, leg_height))

leg_y = y + leg_height // 2

# Левая лапа
leg_x = x - width // 4
ellipse(screen, GRAY, (leg_x - (width // 4) // 2, leg_y - leg_height // 2, width // 4, leg_height))

# Правая лапа
leg_x = x + width // 4
ellipse(screen, GRAY, (leg_x - (width // 4) // 2, leg_y - leg_height // 2, width // 4, leg_height))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()