import turtle
import time

turtle.speed(100)
turtle.color("cyan")
turtle.bgcolor("black")

n = 10

b = 200
while b > 0:
    turtle.left(b)
    turtle.forward(b * 3)
    b = b - 1

time.sleep(n)