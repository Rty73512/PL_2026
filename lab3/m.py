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

def draw_body(screen, x, y, width, height, color):
    """
    Рисует тело зайца
    screen- объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    """
    body_width = width // 2
    body_height = height // 2
    body_y = y + body_height // 2
    ellipse(screen, color, (x - body_width // 2, body_y - body_height // 2, body_width, body_height))

def draw_head(screen, x, y, head_size, color):
    """
    Рисует голову зайца
    screen- объект pygame.Surface
    x, y - координаты центра изображения
    head_size - размер изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    """
    head_y = y - head_size // 2
    circle(screen, color, (x, head_y), head_size // 2)

def draw_ear(screen, x, y, ear_width, ear_height, ear_offset, color, outline_color):
    """
    Рисует одно ухо зайца
    screen - объект pygame.Surface
    x, y - координаты центра изображения
    ear_width, ear_height - ширина и высота уха
    ear_offset - смещение уха от центра по оси X
    color - цвет заливки уха
    outline_color - цвет контура уха
    """
    ear_x = x + ear_offset
    ear_y = y - height // 2 + ear_height // 2
    ellipse(screen, color, (ear_x - ear_width // 2, ear_y - ear_height // 2, ear_width, ear_height))
    ellipse(screen, outline_color, (ear_x - ear_width // 2, ear_y - ear_height // 2, ear_width, ear_height), 2)

def draw_eyes(screen, x, head_y, eye_offset, eye_size):
    """
    Рисует глаза с бликами
    screen - объект pygame.Surface
    x - координата центра изображения по оси X
    head_y - координата головы по оси Y
    eye_offset - смещение глаз от центра
    eye_size - размер глаза
    """
    # Левый глаз
    eye_x = x - eye_offset
    draw_eye(screen, eye_x, head_y, eye_size)
    
    # Правый глаз
    eye_x = x + eye_offset
    draw_eye(screen, eye_x, head_y, eye_size)

def draw_eye(screen, eye_x, eye_y, eye_size):
    """
    Рисует один глаз с бликом
    screen - объект pygame.Surface
    eye_x, eye_y - координаты центра глаза
    eye_size - размер глаза
    """
    circle(screen, WHITE, (eye_x, eye_y - 5), eye_size // 2)  # Белок
    circle(screen, BLACK, (eye_x, eye_y - 5), eye_size // 4)  # Зрачок
    circle(screen, WHITE, (eye_x - 2, (eye_y - 5) - 2), 2)    # Блик

def draw_nose(screen, x, head_y):
    """
    Рисует нос
    screen - объект pygame.Surface
    x - координата центра изображения по оси X
    head_y - координата головы по оси Y
    """
    nose_y = head_y + 10
    circle(screen, BLACK, (x, nose_y), 3)

def draw_mouth(screen, x, head_y):
    """
    Рисует рот
    screen - объект pygame.Surface
    x - координата центра изображения по оси X
    head_y - координата головы по оси Y
    """
    nose_y = head_y + 10
    line(screen, BLACK, (x, nose_y + 3), (x - 5, nose_y + 10), 2)
    line(screen, BLACK, (x, nose_y + 3), (x + 5, nose_y + 10), 2)

def draw_leg(screen, x, y, width, height, leg_offset):
    """
    Рисует одну ногу
    screen - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - общая ширина и высота зайца
    leg_offset - смещение ноги от центра по оси X
    """
    leg_height = height // 16
    leg_y = y + height // 2 - leg_height // 2
    leg_x = x + leg_offset
    leg_width = width // 4
    ellipse(screen, GRAY, (leg_x - leg_width // 2, leg_y - leg_height // 2, leg_width, leg_height))

def draw_rabbit(screen, x, y, width, height):
    """
    Основная функция для рисования всего зайца
    screen - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - общая ширина и высота зайца
    """
    head_size = height // 4
    head_y = y - head_size // 2
    ear_height = height // 3
    ear_width = width // 8
    
    # Рисуем части тела
    draw_body(screen, x, y, width, height, GRAY)
    draw_head(screen, x, y, head_size, GRAY)
    
    # Рисуем уши
    draw_ear(screen, x, y, ear_width, ear_height, -head_size // 4, GRAY, DARK_GRAY)
    draw_ear(screen, x, y, ear_width, ear_height, head_size // 4, GRAY, DARK_GRAY)
    
    # Рисуем глаза
    draw_eyes(screen, x, head_y, head_size // 4, head_size // 3)
    
    # Рисуем нос и рот
    draw_nose(screen, x, head_y)
    draw_mouth(screen, x, head_y)
    
    # Рисуем ноги
    draw_leg(screen, x, y, width, height, -width // 4)
    draw_leg(screen, x, y, width, height, width // 4)

# Координаты центра и размеры зайца
x, y = 200, 200
width, height = 200, 400

# Рисуем зайца
draw_rabbit(screen, x, y, width, height)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()