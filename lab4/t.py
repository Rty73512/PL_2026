import pygame
from pygame.draw import *
from random import randint
import math

pygame.init()

# Константы
FPS = 60
WIDTH = 1000
HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Цвета
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

# Глобальные переменные
balls = []
score = 0
level = 1
combo = 0
last_hit_time = 0
target_score = [5, 15, 30, 50, 80]
initial_balls = [2, 4, 6, 8, 10]

def new_ball():
    """создает новый шарик"""
    x = randint(50, WIDTH - 50)
    y = randint(50, HEIGHT - 50)
    r = randint(20, 50)
    vx = randint(-5, 5)
    vy = randint(-5, 5)
    color = COLORS[randint(0, 5)]
    return [x, y, r, vx, vy, color]

def init_level():
    """инициализация уровня"""
    global balls, last_hit_time, level, score, combo
    balls = []
    num_balls = initial_balls[level - 1]
    for _ in range(num_balls):
        balls.append(new_ball())
    last_hit_time = pygame.time.get_ticks()
    combo = 0

def draw_balls():
    """рисует все шарики"""
    for ball in balls:
        circle(screen, ball[5], (ball[0], ball[1]), ball[2])

def move_balls():
    """перемещает все шарики и обрабатывает отскоки от стен"""
    for ball in balls:
        ball[0] += ball[3]
        ball[1] += ball[4]
        
        if ball[0] - ball[2] <= 0 or ball[0] + ball[2] >= WIDTH:
            ball[3] = -ball[3]
            ball[0] = max(ball[2], min(WIDTH - ball[2], ball[0]))
        
        if ball[1] - ball[2] <= 0 or ball[1] + ball[2] >= HEIGHT:
            ball[4] = -ball[4]
            ball[1] = max(ball[2], min(HEIGHT - ball[2], ball[1]))

def reflect_balls():
    """отражение шариков друг от друга - просто меняем направления"""
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            # Вычисляем расстояние между центрами шариков
            dx = balls[i][0] - balls[j][0]
            dy = balls[i][1] - balls[j][1]
            distance = math.sqrt(dx**2 + dy**2)
            
            # Если шарики столкнулись
            if distance < balls[i][2] + balls[j][2]:
                # Просто меняем направления движения обоих шаров
                balls[i][3] = -balls[i][3]
                balls[i][4] = -balls[i][4]
                balls[j][3] = -balls[j][3]
                balls[j][4] = -balls[j][4]
                
                # Раздвигаем шарики, чтобы они не застревали друг в друге
                overlap = balls[i][2] + balls[j][2] - distance
                if overlap > 0:
                    # Направление от одного шара к другому
                    if distance > 0:
                        nx = dx / distance
                        ny = dy / distance
                        correction = overlap / 2
                        balls[i][0] += nx * correction
                        balls[i][1] += ny * correction
                        balls[j][0] -= nx * correction
                        balls[j][1] -= ny * correction

def update_speed():
    """обновление скорости шариков в зависимости от уровня"""
    global level
    for ball in balls:
        speed = math.sqrt(ball[3]**2 + ball[4]**2)
        if speed > 0:
            ball[3] = (ball[3] / speed) * (5 + level * 1.5)
            ball[4] = (ball[4] / speed) * (5 + level * 1.5)

def check_hit(event):
    """проверяет попадание в шарик"""
    global score, combo, last_hit_time, balls, level
    click_pos = event.pos
    hit_index = -1
    
    for i in range(len(balls) - 1, -1, -1):
        ball = balls[i]
        distance = math.sqrt((click_pos[0] - ball[0])**2 + (click_pos[1] - ball[1])**2)
        
        if distance <= ball[2]:
            hit_index = i
            break
    
    if hit_index >= 0:
        last_hit_time = pygame.time.get_ticks()
        combo += 1
        
       
        points = 10
        score += points
        
        balls.pop(hit_index)
        
        max_balls = initial_balls[level - 1] + (len(balls) * 2)
        if len(balls) < max_balls:
            for _ in range(2):
                balls.append(new_ball())
        
        update_speed()
    else:
        combo = 0

def check_level_up():
    """проверка перехода на следующий уровень"""
    global level, score, combo
    if level < 5 and score >= target_score[level - 1]:
        level += 1
        init_level()
        update_speed()
        return True
    return False

def check_timer_explosion():
    """проверка таймера взрыва (если долго нет попаданий)"""
    global balls, level, last_hit_time
    current_time = pygame.time.get_ticks()
    time_without_hit = (current_time - last_hit_time) / 1000
    
    explosion_time = max(3, 10 - level)
    
    # Если время без попаданий превысило время до взрыва
    if time_without_hit >= explosion_time:
        balls = []
        num_balls = initial_balls[level - 1]
        for _ in range(num_balls):
            balls.append(new_ball())
        update_speed()
        last_hit_time = current_time

def draw_ui():
    """отрисовка интерфейса (счет, уровень, таймер и комбо)"""
    global score, level, combo, last_hit_time
    font = pygame.font.Font(None, 36)
    font_combo = pygame.font.Font(None, 32)
    
    # Счет
    text_surface = font.render(f"Счёт: {score}", True, WHITE)
    screen.blit(text_surface, (10, 10))
    
    # Уровень
    text_surface = font.render(f"Уровень: {level}", True, WHITE)
    screen.blit(text_surface, (10, 50))
    
    # Таймер взрыва (постоянно отображается)
    current_time = pygame.time.get_ticks()
    time_without_hit = (current_time - last_hit_time) / 1000
    explosion_time = max(3, 10 - level)
    
    remaining = max(0, explosion_time - time_without_hit)
    
    text_surface = font.render(f"До взрыва: {remaining:.1f} сек", True, WHITE)
    screen.blit(text_surface, (10, 90))
    
    # Комбо (отображается под таймером)
    if combo >= 0:
        # Выбор текста в зависимости от комбо
        if combo >= 10:
            combo_text = f"КОМБО: x{combo} !!!"
            combo_color = YELLOW
        elif combo >= 5:
            combo_text = f"КОМБО: x{combo} !!"
            combo_color = MAGENTA
        elif combo >= 3:
            combo_text = f"КОМБО: x{combo} !"
            combo_color = CYAN
        elif combo >= 2:
            combo_text = f"КОМБО: x{combo}"
            combo_color = GREEN
        else:
            combo_text = f"КОМБО: x{combo}"
            combo_color = WHITE
        
        text_surface = font_combo.render(combo_text, True, combo_color)
        screen.blit(text_surface, (10, 130))
        
        # Отображение информации о комбо (без бонусных очков)
        if combo >= 2:
            font_small = pygame.font.Font(None, 24)
            info_text = f"Серия: {combo} попаданий подряд!"
            text_surface = font_small.render(info_text, True, combo_color)
            screen.blit(text_surface, (10, 165))

# Инициализация игры
init_level()
clock = pygame.time.Clock()
finished = False

# Основной игровой цикл
while not finished:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                check_hit(event)
                check_level_up()
    
    move_balls()
    reflect_balls()
    check_timer_explosion()
    
    screen.fill(BLACK)
    draw_balls()
    draw_ui()
    pygame.display.update()

pygame.quit()