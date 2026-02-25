from turtle import *
from random import *
# # task 1
# a = 179
# b = 197
# c = (a ** 2 + b ** 2) ** 0.5
# print (c)

# # task 2
# import turtle

# turtle.shape('turtle')
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(50)

# # task 3
# from turtle import *
# fd(100)
# rt(90)
# fd(100)
# rt(90)
# fd(100)
# rt(90)
# fd(100)

# # task 4
# for i in range(360):
#     fd(2)
#     lt(1)
# input()


# # task 5
# c = 0
# l = 30
# while c!=9:
#     up()
#     goto(0-4*c,0-4*c)
#     down()
#     fd(l)
#     lt(90)
#     fd(l)
#     lt(90)
#     fd(l)
#     lt(90)
#     fd(l)
#     lt(90)
#     l+=8
#     c+=1


# # task 6
# # n = int(input("Введите n: "))
# n = 12
# c = 0
# while c!=n:
#     rt(360/n)
#     fd(100)
#     stamp()
#     goto(0,0)
#     c+=1


# task 7
# l = 0
# while l!=200:
#     fd(l) 
#     lt(10)
#     l += 0.1


# # task 8
# l = 10
# while l!=400:
#     fd(l)
#     lt(90)
#     l+=5


# # task 9
# import math

# speed(10)

# def drw(n, l):
#     p = 360 / n
#     for i in range(n):
#         fd(l)
#         lt(p)

# n = 3
# a = 50

# for i in range(10):
#     R = a / (2 * math.sin(math.radians(180 / n)))
#     up()
#     goto(0, 0)  # центр
#     setheading(90)  # смотрит вверх
#     bk(R)  # от центра вниз к нижней вершине
#     rt(90 - 180/n)  # поворот для начала рисования стороны
#     down()
#     drw(n, a)
#     n += 1
#     a += 15

# done()


# # task 10
# def cir(r, i):
#     if i%2==0:
#         for i in range(72):
#             fd(r)
#             lt(5)
#     else:
#         for i in range(72):
#             fd(r)
#             rt(5)
# for x in range(3):
#     cir(5, 2)
#     cir(5, 1)
#     lt(60)


# # task 11
# def cir(r, i):
#     if i%2==0:
#         for i in range(72):
#             fd(r)
#             lt(5)
#     else:
#         for i in range(72):
#             fd(r)
#             rt(5)
# lt(90)
# r = 5
# for x in range(10):
#     cir(r,2)
#     cir(r,1)
#     r+=2


# # task 12
# def dug(r, i):
#     if i%2==0:
#         for i in range(180):
#             fd(r)
#             lt(1)
#     else:
#         for i in range(180):
#             fd(r)
#             rt(1)
# lt(90)
# for x in range(20):
#     dug(1, 2)
#     dug(0.1, 2)


# # task 13
# def cir(r, i):
#     if i%2==0:
#         for i in range(72):
#             fd(r)
#             lt(5)
#     else:
#         for i in range(72):
#             fd(r)
#             rt(5)


# def dug(r, i,u):
#     if i%2==0:
#         for i in range(int(180/u)):
#             fd(r)
#             lt(u)
#     else:
#         for i in range(int(180/u)):
#             fd(r)
#             rt(u)
# # лицо
# fillcolor("yellow")
# begin_fill()
# cir(10,2)
# end_fill()

# #глаз левый
# up()
# fillcolor("blue")
# goto(-60, 150)
# down()
# begin_fill()
# cir(2,2)
# end_fill()

# #лаз левый
# up()
# fillcolor("blue")
# goto(60, 150)
# down()
# begin_fill()
# cir(2,2)
# end_fill()

# # нос
# up()
# goto(5, 100)
# down()
# rt(90)
# pensize(10)
# fd(30)
# up()

# #рот
# goto(50, 70)
# color("red")
# down()
# dug(7, 1, 10)
# done()


# # task 14
# def z(l, n):
#     if n%2!=0:
#         i = 0
#         for i in range(n):
#             fd(l)
#             rt(180-180/n)
#     else:
#         i = 0
#         for i in range(2*n):
#             fd(l)
#             rt(180-180/n)
# z(100, 3)
# done()


# # task 15
# from random import randint
# for x in range(100):
#     rt(randint(0, 90))
#     fd(randint(0, 100))


# # task 16 -17
# file = open("file.txt", "r")
# speed(3)

# DIGITS = {
#     '1': [(0, 50), (50, 100), (50, 0)],
#     '2': [(0, 100), (50, 100), (50, 50), (0, 0), (50, 0)],
#     '3': [(0, 100), (50, 100), (0, 50), (50, 50), (0, 0)],
#     '4': [(0, 100), (0, 50), (50, 50), (50, 100), (50, 0)],
#     '5': [(50, 100), (0, 100), (0, 50), (50, 50), (50, 0), (0, 0)],
#     '6': [(50, 100), (0, 50), (0, 0), (50, 0), (50, 50), (0, 50)],
#     '7': [(0, 100), (50, 100), (0, 50), (0, 0)],
#     '8': [(0, 0), (0, 100), (50, 100), (50, 0), (0, 0), (0, 50), (50, 50)],
#     '9': [(50, 50), (0, 50), (0, 100), (50, 100), (50, 0), (0, 0)],
#     '0': [(0, 0), (0, 100), (50, 100), (50, 0), (0, 0), (50, 100)]
# }


# def draw_digit(digit, start_x, start_y):
#     if digit not in DIGITS:
#         return
#     coords = DIGITS[digit]
#     up()
#     goto(start_x + coords[0][0], start_y + coords[0][1])
#     down()
#     for x, y in coords[1:]:
#         goto(start_x + x, start_y + y)


# def draw_index(index_string):
#     x_offset = -300
#     y_offset = 0
#     spacing = 70
#     for char in index_string:
#         draw_digit(char, x_offset, y_offset)
#         x_offset += spacing



# my_index =file.read()
# file.close()

# draw_index(my_index)
# done()

# # task 18

# WIDTH = 400
# HEIGHT = 400
# number_of_turtles = 10
# steps_of_time = 50

# pool = [Turtle(shape='circle') for i in range(number_of_turtles)]

# for unit in pool:
#     unit.up()
#     unit.speed(0)
#     unit.shapesize(0.5)
#     unit.goto(randint(-WIDTH // 2 + 20, WIDTH // 2 - 20), randint(-HEIGHT // 2 + 20, HEIGHT // 2 - 20))
#     unit.setheading(randint(0, 360))

# border = Turtle()
# border.hideturtle()
# border.up()
# border.goto(-WIDTH // 2, -HEIGHT // 2)
# border.pendown()
# for i in range(2):
#     border.forward(WIDTH)
#     border.left(90)
#     border.forward(HEIGHT)
#     border.left(90)

# for u in range(steps_of_time):
#     for unit in pool:
#         unit.forward(3)
#         x, y = unit.pos()
#         if x > WIDTH // 2 or x < -WIDTH // 2:
#             unit.setheading(180 - unit.heading())
#         if y > HEIGHT // 2 or y < -HEIGHT // 2:
#             unit.setheading(-unit.heading())
# done()

