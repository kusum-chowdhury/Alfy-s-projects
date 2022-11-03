import turtle
from turtle import *

# creating haxagon
turtle = turtle.Turtle()
def triangle(edge=100):
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.left(300)

triangle()
triangle()
triangle()
triangle()
triangle()
triangle()