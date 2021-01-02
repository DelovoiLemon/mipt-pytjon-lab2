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
    for j in range(0, n, 10):
            turtle.forward(side_length * j)
            turtle.left(90)


turtle.shape('turtle')
spiral(0, 0, 300, 1)

input()
