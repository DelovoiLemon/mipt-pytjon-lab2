#!/bin/python3

import turtle

def draw_spider(n, paw_length):
    """ Данная функция рисует "паука"
        n - количество лап
        paw_length - длинна лапы        
    """
    turtle.shape('turtle')
    for i in range(n):
        turtle.forward(paw_length)
        turtle.stamp()
        turtle.right(180)
        turtle.forward(paw_length)
        turtle.right(180 - (360 /  n))


draw_spider(12, 100)

input()
