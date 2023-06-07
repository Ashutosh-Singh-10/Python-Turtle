import turtle
turtle.speed(1000)
turtle.bgcolor("black")
x=100
angle=120
colors=["red","red","yellow"]
for i in range(1000):
    turtle.color(colors[int(i%3)])
    turtle.fd(x)
    turtle.right(angle)
    if(i%3==0):
        turtle.right(10)
    x+=1    
