import turtle
import random
from turtle import *

turtle = turtle.Turtle()
def rectangle():
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(100)
  turtle.right(90)



rectangle()
turtle.circle(30)
turtle.circle(15)
turtle.forward(100)
turtle.circle(30)
turtle.circle(15)

turtle.penup()
# making eyes
turtle.right(150)
turtle.forward(30)
turtle.pendown()
turtle.circle(10)
turtle.penup()
turtle.left(180)
turtle.forward(30)
turtle.left(150)
turtle.forward(100)


turtle.left(120)
turtle.forward(30)
turtle.pendown()
turtle.circle(10)
turtle.penup()
turtle.left(180)
turtle.forward(30)
turtle.left(150)
turtle.forward(45)
turtle.left(90)

# making nose
turtle.forward(50)
turtle.right(120)
turtle.pendown()
turtle.forward(10)
turtle.left(120)
turtle.forward(10)
turtle.left(120)
turtle.forward(10)
turtle.penup()
turtle.left(60)
turtle.forward(50)
turtle.left(90)

# making smile
turtle.forward(25)
turtle.left(90)
turtle.forward(30)
turtle.right(90)
turtle.pendown()
turtle.circle(20,180)
turtle.penup()
turtle.right(90)
turtle.forward(30)
