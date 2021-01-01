#!/bin/python3

import turtle

def polygon(x, y, n, side_length):
    """ Данная функция риcует фигуру
        (x, y) - координата левого нижнего угла
        n - количество сторон 
        side_length - длина одной стороны
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(n):
        turtle.forward(side_length)
        turtle.left(360 / n)


turtle.shape('turtle')
polygon(100, 100, 4, 100)

input()
