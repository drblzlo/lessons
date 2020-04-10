# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

step_x = 20
step_y = 10


def brick_build(x=0, y=0, brick_width=step_x, brick_height=step_y):
    dot_x = sd.get_point(x, y)
    dot_y = sd.get_point(x + brick_width, y)
    sd.line(dot_x, dot_y)

    dot_x = sd.get_point(x + brick_width, y)
    dot_y = sd.get_point(x + brick_width, y + brick_height)
    sd.line(dot_x, dot_y)

    dot_x = sd.get_point(x + brick_width, y + brick_height)
    dot_y = sd.get_point(x, y + brick_height)
    sd.line(dot_x, dot_y)

    dot_x = sd.get_point(x, y + brick_height)
    dot_y = sd.get_point(x, y)
    sd.line(dot_x, dot_y)

def brick_wall(x=0, y=0):
    line_number = 0
    x_for_while = x
    while y <= 600:
        if line_number % 2:
            x = x_for_while - step_x / 2
        else:
            x = x_for_while
        while x <= 600:
            brick_build(x=x, y=y)
            x += step_x
        y += step_y
        line_number += 1

brick_wall()

sd.clear_screen()

line_number, i = 0, 0
while i <= 600:
    if line_number % 2:
        j = 0 - step_x / 2
    else:
        j = 0
    dot_a = sd.get_point(j, i)
    dot_b = sd.get_point(600, i)
    sd.line(dot_a, dot_b)
    while j <= 600:
        dot_a = sd.get_point(j, i)
        dot_b = sd.get_point(j, i + step_y)
        sd.line(dot_a, dot_b)
        j += step_x
    i += step_y
    line_number += 1

sd.pause()
