import turtle
from turtle import *
speed(1000)
turtle.up()
turtle.left(90)
turtle.fd(250)
turtle.down()
turtle.left(90)
color("black","black")
begin_fill()
for a in range(0,360):
    turtle.left(1)
    turtle.fd(3)
end_fill()
color("black","white")
begin_fill()

for a in range(0,180):
    turtle.fd(1.5)
    turtle.left(1)

for a in range(0,180):
    turtle.fd(1.5)
    turtle.right(1)
for a in range(0,180):
    turtle.fd(3)
    turtle.right(1)
    
end_fill()
turtle.up()
turtle.right(90)
turtle.fd(21)
turtle.left(90)
turtle.fd(42)
turtle.down()
begin_fill()
for a in range(0,360):
    turtle.fd(0.75)
    turtle.right(1)
end_fill()
turtle.up()
turtle.left(180)
turtle.right(90)
turtle.fd(21)
turtle.left(90)
turtle.fd(42)
turtle.right(180)
for a in range(0,180):
    turtle.fd(3)
    turtle.right(1)
turtle.right(90)
turtle.fd(21)
turtle.left(90)
turtle.fd(42)
turtle.down()
color("black","black")
begin_fill()
for a in range(0,360):
    turtle.fd(0.75)
    turtle.right(1)
end_fill()
