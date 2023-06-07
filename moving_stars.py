import turtle
import random
import sys
li_color=["red","blue","yellow","green","white","brown","orange","pink","violet","purple"]
li=list()
star_color=list()
def coloring():
    for x in range(0,201):
        star_color.append(random.choice(li_color))
def random_value(star_turtle):
    a=random.randrange(0,360)
    b=random.random()
    star_turtle.left(a)
    star_turtle.fd(1)
    
def circle_creating(star_turtle,colour,n):
    star_turtle.hideturtle()
    star_turtle.color("black",colour)
    star_turtle.begin_fill()
    star_turtle.circle(n)
    star_turtle.end_fill()
def star_creating(star_turtle,colour,n):
    star_turtle.hideturtle()
    star_turtle.color("black",colour)
    star_turtle.begin_fill()
    for b in range(4):
        star_turtle.fd(n)
        star_turtle.left(300)
        star_turtle.fd(n)
        star_turtle.right(210)
    star_turtle.end_fill()


this=sys.modules[__name__]
for x in range(0,200):
    li.append(setattr(this,'string%s' % x,"hello"))
for x in range(0,200):
    li[x]=turtle.Turtle()

def stars():
    coloring()
    screen=turtle.Screen()
    screen.tracer(0)
    screen.bgcolor("black")
    for x in range(0,200):
        d=random.randrange(-500,500)
        e=random.randrange(-500,500)
        li[x].goto(d,e)
    check=0
    while True:
        for x in range(0,200):
            li[x].clear()
        for x in range(0,200):
            if check%2==0:
                circle_creating(li[x],star_color[x],3)
            else:
                star_creating(li[x],star_color[x],5)
        screen.update()
        for x in range(0,200):
            random_value(li[x])
        check+=1
stars()
