import turtle
import webcolors
import colorsys

#Establecemos el color de fondo
turtle.bgcolor("Black")

#Establecemos la velocidad de dibujo del patrón
turtle.speed(0)

n = 36
h = 0

#Loop
for i in range(460):
    c = colorsys.hsv_to_rgb(h,1,0.9)
    h+=1/n
    turtle.color(c)
    turtle.left(145)
    for j in range(5):
        turtle.forward(300)
        turtle.left(150)