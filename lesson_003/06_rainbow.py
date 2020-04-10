# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd
#sd.resolution = (1200, 600)
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
def rainbow(point,radius):
     for i in range(7):
        radius += 5
        color = sd.random_color()
        sd.circle(point, radius, rainbow_colors[i], 4)

point = sd.get_point(350, 50)
radius = sd.randint(300, 400)

rainbow(point, radius)
point1 = sd.get_point(0, 0)
point2 = sd.get_point(50, 600)
sd.rectangle(point1, point2, color=sd.background_color)

point3 = sd.get_point(350, 0)
point4 = sd.get_point(600, 600)
sd.rectangle(point3, point4, color=sd.background_color)



# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво





sd.pause()
