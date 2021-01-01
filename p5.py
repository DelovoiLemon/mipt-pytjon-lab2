#!/bin/python3

import turtle

def draw_polygon(x, y, n, side_length):
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


def draw_nested_poly(x, y, side_length, attachment_count, distance):
    """ Данная функция рисует вложенные квадраты
        (x, y) - левый нижний угол самого маленького квадрата
        side_length - длинна стороны самого маленького квадрата
        attachment_count - количество вложенных квадратов
        distance - дистанция между квадратами
    """

    for j in range(attachment_count):
        draw_polygon(x - (distance * j), y - (distance * j), 
                     4, side_length + (distance * j * 2))



turtle.shape('turtle')
draw_nested_poly(0, 0, 50, 10, 25)

input()
