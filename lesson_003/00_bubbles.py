# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# point = sd.get_point(sd.randint(1,1200), sd.randint(1,600))
# radius = sd.randint(25, 250)
# for _ in range(3):
#     radius += 5
#     color = sd.random_color()
#     sd.circle(point, radius, color, 1)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def bubble(point,radius):
    for _ in range(7):
        radius += 5  # sd.randint(25, 75)
        color = sd.random_color()
        sd.circle(point, radius, color, 1)

# for _ in range(sd.randint(50, 2000)):
#     point = sd.get_point(sd.randint(1, 1200), sd.randint(1, 600))
#     radius = sd.randint(25, 250)
#     bubble(point, radius)


# Нарисовать 10 пузырьков в ряд
# x = sd.randint(1, 120)
# y = sd.randint(1, 600)
# point = sd.get_point(x, y)
# radius = sd.randint(25, 250)
# for _ in range(10):
#     bubble(point, radius)
#     x += sd.randint(30, 200)
#     point = sd.get_point(x, y)

# Нарисовать три ряда по 10 пузырьков

# radius = sd.randint(25, 100)
# lists_of_x = []
# for i in range(10):
#     lists_of_x.append(sd.randint(30, 175))
# lists_of_y = []
# for i in range(3):
#     lists_of_y.append(sd.randint(30, 175))
# x_copy = x = sd.randint(1, 120)
# y = sd.randint(1, 200)
# for j in range(3):
#     x = x_copy
#     y += lists_of_y[j]
#     for i in range(10):
#         x += lists_of_x[i]
#         point = sd.get_point(x, y)
#         bubble(point, radius)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for i in range(101):
    point = sd.get_point(sd.randint(1, 1200), sd.randint(1, 600))
    radius = sd.randint(25, 250)
    bubble(point, radius)
    #print(i)
sd.pause()
