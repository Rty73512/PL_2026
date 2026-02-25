import pygame
import sys
import math

pygame.init()
screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption("7 котов и клубков с 3 окнами")

clock = pygame.time.Clock()

# Цвета
floor_color = (139, 69, 19)        # тёмно-коричневый (пол)
wall_color = (205, 133, 63)        # светло-коричневый (стены)
cat_orange = (255, 140, 0)         # рыжий кот
cat_dark_orange = (200, 100, 0)    # тени кота
cat_black = (30, 30, 30)            # детали кота (глаза, усы)
yarn_brown = (160, 82, 45)         # клубок коричневый
window_blue = (135, 206, 250)      # цвет стекла окна
window_frame = (100, 70, 40)       # рама окна

def draw_floor_and_walls():
    pygame.draw.rect(screen, wall_color, (0, 0, 900, 180))   # стена
    pygame.draw.rect(screen, floor_color, (0, 180, 900, 320))  # пол

def draw_cat(x, y):
    pygame.draw.ellipse(screen, cat_orange, (x, y, 180, 90))  # тело
    pygame.draw.circle(screen, cat_orange, (x + 150, y + 30), 40)  # голова

    pygame.draw.polygon(screen, cat_dark_orange, [(x + 125, y + 5), (x + 140, y - 30), (x + 160, y - 10)])  # левое ухо
    pygame.draw.polygon(screen, cat_dark_orange, [(x + 180, y + 5), (x + 195, y - 30), (x + 215, y - 10)])  # правое ухо

    pygame.draw.ellipse(screen, (255, 255, 255), (x + 130, y + 20, 20, 15))  # левый глаз белок
    pygame.draw.ellipse(screen, (255, 255, 255), (x + 160, y + 20, 20, 15))  # правый глаз белок
    pygame.draw.circle(screen, cat_black, (x + 140, y + 27), 6)  # левый зрачок
    pygame.draw.circle(screen, cat_black, (x + 170, y + 27), 6)  # правый зрачок

    pygame.draw.polygon(screen, cat_dark_orange, [(x + 155, y + 45), (x + 145, y + 55), (x + 165, y + 55)])  # нос

    pygame.draw.line(screen, cat_black, (x + 130, y + 55), (x + 100, y + 50), 2)  # усы левые
    pygame.draw.line(screen, cat_black, (x + 130, y + 60), (x + 100, y + 60), 2)
    pygame.draw.line(screen, cat_black, (x + 180, y + 55), (x + 210, y + 50), 2)  # усы правые
    pygame.draw.line(screen, cat_black, (x + 180, y + 60), (x + 210, y + 60), 2)

def draw_yarn_ball(x, y, radius):
    pygame.draw.circle(screen, yarn_brown, (x, y), radius)

    for i in range(0, 360, 30):
        angle_rad = math.radians(i)
        start_x = x + int(radius * math.cos(angle_rad))
        start_y = y + int(radius * math.sin(angle_rad))
        end_x = x + int(radius * 0.5 * math.cos(angle_rad + 0.4))
        end_y = y + int(radius * 0.5 * math.sin(angle_rad + 0.4))
        pygame.draw.line(screen, (120, 50, 20), (start_x, start_y), (end_x, end_y), 2)

    pygame.draw.circle(screen, (120, 50, 20), (x, y), int(radius*0.7), 2)
    pygame.draw.circle(screen, (120, 50, 20), (x, y), int(radius*0.4), 2)

def draw_window(x, y, width=80, height=100):
    # Рама окна (коричневый прямоугольник)
    pygame.draw.rect(screen, window_frame, (x, y, width, height))
    # Стекло - внутренняя часть (голубой прямоугольник чуть меньше)
    pygame.draw.rect(screen, window_blue, (x + 10, y + 10, width - 20, height - 20))
    # Перекрестие рамы окна (делит стекло на 4 части)
    pygame.draw.line(screen, window_frame, (x + width//2, y + 10), (x + width//2, y + height - 10), 3)
    pygame.draw.line(screen, window_frame, (x + 10, y + height//2), (x + width - 10, y + height//2), 3)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    draw_floor_and_walls()

    # Рисуем 3 окна на стене, равномерно
    window_positions = [100, 400, 700]
    for wx in window_positions:
        draw_window(wx, 30)

    # Рисуем 7 котов с клубками:
    # по горизонтали с шагом 110, кот слева от клубка на 0 по Y
    start_x = 50
    start_y = 230
    for i in range(7):
        cat_x = start_x + i * 110
        cat_y = start_y
        draw_cat(cat_x, cat_y)
        draw_yarn_ball(cat_x + 200, cat_y + 70, 30)  # клубок справа от кота

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()