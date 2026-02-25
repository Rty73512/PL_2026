import pygame
import sys
import math

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Рыжий кот и клубок в интерьере")

clock = pygame.time.Clock()

# Цвета
floor_color = (139, 69, 19)        # тёмно-коричневый (пол)
wall_color = (205, 133, 63)        # светло-коричневый (стены)
cat_orange = (255, 140, 0)         # рыжий кот
cat_dark_orange = (200, 100, 0)    # тёмные части кота (тени)
cat_black = (30, 30, 30)            # детали кота (глаза, усы)
yarn_brown = (160, 82, 45)         # клубок коричневый

def draw_floor_and_walls():
    # Стена (верхняя часть)
    pygame.draw.rect(screen, wall_color, (0, 0, 600, 150))
    # Пол (нижняя часть)
    pygame.draw.rect(screen, floor_color, (0, 150, 600, 250))

def draw_cat(x, y):
    # Тело кота - лежащая овальная форма
    pygame.draw.ellipse(screen, cat_orange, (x, y, 180, 90))
    # Голова - круг
    pygame.draw.circle(screen, cat_orange, (x + 150, y + 30), 40)

    # Тени и уши
    pygame.draw.polygon(screen, cat_dark_orange, [(x + 125, y + 5), (x + 140, y - 30), (x + 160, y - 10)])  # левое ухо
    pygame.draw.polygon(screen, cat_dark_orange, [(x + 180, y + 5), (x + 195, y - 30), (x + 215, y - 10)])  # правое ухо

    # Глаза — два овала с зрачками
    pygame.draw.ellipse(screen, (255, 255, 255), (x + 130, y + 20, 20, 15))
    pygame.draw.ellipse(screen, (255, 255, 255), (x + 160, y + 20, 20, 15))
    pygame.draw.circle(screen, cat_black, (x + 140, y + 27), 6)
    pygame.draw.circle(screen, cat_black, (x + 170, y + 27), 6)

    # Нос — треугольник
    pygame.draw.polygon(screen, cat_dark_orange, [(x + 155, y + 45), (x + 145, y + 55), (x + 165, y + 55)])

    # Усы — линии
    pygame.draw.line(screen, cat_black, (x + 130, y + 55), (x + 100, y + 50), 2)
    pygame.draw.line(screen, cat_black, (x + 130, y + 60), (x + 100, y + 60), 2)
    pygame.draw.line(screen, cat_black, (x + 180, y + 55), (x + 210, y + 50), 2)
    pygame.draw.line(screen, cat_black, (x + 180, y + 60), (x + 210, y + 60), 2)

def draw_yarn_ball(x, y, radius):
    # Круг клубка
    pygame.draw.circle(screen, yarn_brown, (x, y), radius)

    # Несколько нитей (кривые линии)
    for i in range(0, 360, 30):
        angle_rad = math.radians(i)
        start_x = x + int(radius * math.cos(angle_rad))
        start_y = y + int(radius * math.sin(angle_rad))
        end_x = x + int(radius * 0.5 * math.cos(angle_rad + 0.4))
        end_y = y + int(radius * 0.5 * math.sin(angle_rad + 0.4))
        pygame.draw.line(screen, (120, 50, 20), (start_x, start_y), (end_x, end_y), 2)

    # Дополнительные нитки внутри кругов – имитация клубка
    pygame.draw.circle(screen, (120, 50, 20), (x, y), int(radius*0.7), 2)
    pygame.draw.circle(screen, (120, 50, 20), (x, y), int(radius*0.4), 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    draw_floor_and_walls()
    draw_cat(150, 200)
    draw_yarn_ball(370, 250, 40)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()