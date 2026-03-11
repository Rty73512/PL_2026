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

def draw_ear(screen, x, y, color_main, color_outline, color_inner, ear_width, ear_height):
    """
    Рисует одно ухо зайца.
    
    Аргументы:
        screen: поверхность для рисования
        x, y: координаты центра уха
        color_main: основной цвет уха
        color_outline: цвет контура
        color_inner: цвет внутренней части уха
        ear_width: ширина уха
        ear_height: высота уха
    """
    # Основная часть уха
    ellipse(screen, color_main, (x - ear_width // 2, y - ear_height // 2, ear_width, ear_height))
    # Контур уха
    ellipse(screen, color_outline, (x - ear_width // 2, y - ear_height // 2, ear_width, ear_height), 2)
    # Внутренняя розовая часть
    ellipse(screen, color_inner, (x - ear_width // 4, y - ear_height // 4, ear_width // 2, ear_height // 2))

def draw_eye(screen, x, y, eye_size):
    """
    Рисует один глаз зайца.
    
    Аргументы:
        screen: поверхность для рисования
        x, y: координаты центра глаза
        eye_size: размер глаза
    """
    # Белая часть глаза
    circle(screen, WHITE, (x, y), eye_size // 2)
    # Зрачок
    circle(screen, BLACK, (x, y), eye_size // 4)
    # Блик
    circle(screen, WHITE, (x - 2, y - 2), 2)

def draw_head(screen, x, y, head_size):
    """
    Рисует голову зайца с глазами, носом и ртом.
    
    Аргументы:
        screen: поверхность для рисования
        x, y: координаты центра тела
        head_size: размер головы
    """
    # Голова
    head_y = y - head_size // 2
    circle(screen, GRAY, (x, head_y), head_size // 2)
    
    # Глаза
    eye_size = head_size // 3
    eye_y = head_y - 5
    eye_offset = head_size // 4
    
    draw_eye(screen, x - eye_offset, eye_y, eye_size)  # Левый глаз
    draw_eye(screen, x + eye_offset, eye_y, eye_size)  # Правый глаз
    
    # Нос
    nose_y = head_y + 10
    circle(screen, BLACK, (x, nose_y), 3)
    
    # Рот
    line(screen, BLACK, (x, nose_y + 3), (x - 5, nose_y + 10), 2)
    line(screen, BLACK, (x, nose_y + 3), (x + 5, nose_y + 10), 2)

def draw_ears(screen, x, y, head_size, ear_height, ear_width):
    """
    Рисует оба уха зайца.
    
    Аргументы:
        screen: поверхность для рисования
        x, y: координаты центра тела
        head_size: размер головы
        ear_height: высота ушей
        ear_width: ширина ушей
    """
    # ИСПРАВЛЕНИЕ: уши должны начинаться от верхней части головы
    ear_y = y - head_size // 2 - ear_height // 2
    
    # Левое ухо
    draw_ear(screen, x - head_size // 4, ear_y, GRAY, DARK_GRAY, PINK, ear_width, ear_height)
    # Правое ухо
    draw_ear(screen, x + head_size // 4, ear_y, GRAY, DARK_GRAY, PINK, ear_width, ear_height)

def draw_body(screen, x, y, body_width, body_height):
    """
    Рисует тело зайца.
    
    Аргументы:
        screen: поверхность для рисования
        x, y: координаты центра тела
        body_width: ширина тела
        body_height: высота тела
    """
    body_y = y + body_height // 2
    ellipse(screen, GRAY, (x - body_width // 2, body_y - body_height // 2, body_width, body_height))

def draw_legs(screen, x, y, width, height):
    """
    Рисует ноги и лапы зайца.
    
    Аргументы:
        screen: поверхность для рисования
        x, y: координаты центра тела
        width: общая ширина зайца
        height: общая высота зайца
    """
    leg_height = height // 16
    
    # Нижние ноги
    leg_y = y + height // 2 - leg_height // 2
    
    # Левая нижняя нога
    leg_x = x - width // 4
    ellipse(screen, GRAY, (leg_x - (width // 4) // 2, leg_y - leg_height // 2, width // 4, leg_height))
    
    # Правая нижняя нога
    leg_x = x + width // 4
    ellipse(screen, GRAY, (leg_x - (width // 4) // 2, leg_y - leg_height // 2, width // 4, leg_height))
    
    # Верхние лапы
    leg_y = y + leg_height // 2
    
    # Левая верхняя лапа
    leg_x = x - width // 4
    ellipse(screen, GRAY, (leg_x - (width // 4) // 2, leg_y - leg_height // 2, width // 4, leg_height))
    
    # Правая верхняя лапа
    leg_x = x + width // 4
    ellipse(screen, GRAY, (leg_x - (width // 4) // 2, leg_y - leg_height // 2, width // 4, leg_height))

def draw_hare(screen, x, y, width, height):
    """
    Главная функция для рисования всего зайца целиком.
    
    Аргументы:
        screen: поверхность для рисования
        x, y: координаты центра зайца
        width: общая ширина зайца
        height: общая высота зайца
    """
    # Размеры отдельных частей
    body_width = width // 2
    body_height = height // 2
    head_size = height // 4
    ear_height = height // 3
    ear_width = width // 8
    
    # Рисование всех частей в правильном порядке
    draw_body(screen, x, y, body_width, body_height)
    draw_ears(screen, x, y, head_size, ear_height, ear_width)
    draw_head(screen, x, y, head_size)
    draw_legs(screen, x, y, width, height)

# Координаты центра и размеры зайца
x, y = 200, 200
width, height = 200, 400

# Рисуем зайца одной командой
draw_hare(screen, x, y, width, height)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()