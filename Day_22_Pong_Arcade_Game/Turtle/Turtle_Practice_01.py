from turtle import *

t = Turtle()
screen = Screen()

screen.listen()
# Triangle
# t.penup()
# t.forward(100)
# t.left(120)
# t.forward(100)
# t.left(120)
# t.forward(100)

for steps in range(10, 40):
  for c in ('blue', 'red', 'green'):
    color(c)
    forward(steps)
    right(30)

while True:
  forward(200)
  left(170)
  if abs(pos()) < 1: 
    break

color('red')
fillcolor('yellow')
screen.exitonclick()