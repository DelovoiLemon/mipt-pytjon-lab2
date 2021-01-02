#!/bin/python3

import turtle

def spiral(x, y, n, side_length):
    """ Данная функция риcует фигуру
        (x, y) - координата левого нижнего угла
        n - количество сторон 
        side_length - длина одной стороны
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for j in range(1, n - 1, 1):
            turtle.forward(side_length * j / (n - 1))
            turtle.left(12)


turtle.shape('turtle')
spiral(-100, -100, 100, 50)

input()
