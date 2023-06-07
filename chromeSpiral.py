import turtle
turtle.speed(1000)
turtle.bgcolor("black")
x=1
turtle.color("red")
turtle.penup()
turtle.lt(90)
turtle.fd(100)
turtle.rt(90)
turtle.pendown()
colors=["red","green","blue","yellow"]
angle=0
index=1
for i in range(5000):
    turtle.fd(5)
    turtle.right(x)
    angle+=x
    if angle>90:
        angle=0
        turtle.color(
            colors[index%len(colors)]
        )
        index+=1
    
    x+=0.001


#In the code line 18  we are using floor function(GIF) to make sure there is a rotation in successing spiral.
