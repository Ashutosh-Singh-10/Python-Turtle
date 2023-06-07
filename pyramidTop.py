import turtle
turtle.speed(2000)
turtle.bgcolor("black")
x=10
colors=["red","yellow","blue"]
turtle.right(60)
for i in range(1,10000):
    turtle.color(
        colors[int(i%3)]
    )
    turtle.fd(x)
    turtle.right(120)
    x+=0.5
