#!/bin/python3

import turtle

def draw_polygon(n, side_length):
    """ Данная функция риcует фигуру
        (x, y) - координата левого нижнего угла
        n - количество сторон 
        side_length - длина одной стороны
    """   
    for i in range(n):
        turtle.forward(side_length)
        turtle.left(360 / n)


def draw_regular_poly(n, side_length, step):
    turtle.left(150)
    for i in range(3, n + 1, 1):
        turtle.penup()
        #turtle.left(180 / i)
        #print(i, 360 / i)
        turtle.forward(step * i)
        turtle.left(135 * (i - 3))
        turtle.pendown()
        draw_polygon(i, side_length + step * (i - 3))
        turtle.right(150)

turtle.speed(1)
turtle.shape('turtle')
#draw_polygon(3, 100)
draw_regular_poly(5, 100, 1)

input()
