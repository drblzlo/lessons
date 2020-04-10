# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

sd.resolution = (1200, 600)


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile(x=sd.randint(0, 1200), y=sd.randint(0, 600), color=sd.random_color()):
    smile_cencer = sd.get_point(x, y)
    left_bottom = sd.get_point(x - 100, y - 75)
    right_top = sd.get_point(x + 100, y + 75)
    sd.ellipse(left_bottom, right_top, width=1, color=color)
    left_eye_center = sd.get_point(x - 40, y + 25)
    sd.circle(left_eye_center, 20, color=color)
    right_eye_center = sd.get_point(x + 40, y + 25)
    sd.circle(right_eye_center, 25, color=color)
    point_1 = sd.get_point(x - 50, y - 25)
    point_2 = sd.get_point(x - 25, y - 35)
    point_3 = sd.get_point(x + 25, y - 35)
    point_4 = sd.get_point(x + 50, y - 25)
    point_list = [point_1, point_2, point_3, point_4]
    sd.lines(point_list, color=color)

for _ in range(61):
    smile(x=sd.randint(0, 1200), y=sd.randint(0, 600), color=sd.random_color())
sd.pause()
