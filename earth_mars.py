import turtle
import math
from turtle import *
# from ithchart import Chart
turtle.color("white","white")
i=0
def sun():
    turtle.hideturtle()
    turtle.color("orange","yellow")
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()
class Movement:
    def big_position(li,i,cos_angle1=0,cos_angle2=22/21):
        planet_position=[li[0]*(math.sin((i*li[1])/li[0]))*math.cos(cos_angle1),li[0]*(math.cos((i*li[1])/li[0]))*math.cos(cos_angle2)]
        return planet_position
                     

    def small_position(li,li2,i,cos_angle1=0,cos_angle2=22/21):
        a=Movement.big_position(li2,i)
        small_planet_position=[(a[0]+li[0]*(math.sin((i*li[1])/li[0]))*math.cos(cos_angle1)),(a[1]+li[0]*(1-math.cos((i*li[1])/li[0]))*math.cos(cos_angle2))]
        return small_planet_position

    def planet_turtle(moon_turtle,n,cc):
        moon_turtle.hideturtle()
        moon_turtle.color("black",cc)
        moon_turtle.begin_fill()
        moon_turtle.circle(n)
        moon_turtle.end_fill()
    
class RelativeMotion:
    def __init__(self,li):
        self.li=li
        self.screen=turtle.Screen()
        
    def around_p1(self):
        i=1
        self.screen.tracer(0)
        body1=turtle.Turtle()
        body2=turtle.Turtle()
        body3=turtle.Turtle()
        body4=turtle.Turtle()
        body5=turtle.Turtle()
        body6=turtle.Turtle()
        body7=turtle.Turtle()
        while True:
            body1.clear()
            body3.clear()
            body4.clear()
            body2.clear()
            body5.clear()
            body6.clear()
            body7.clear()
            Movement.planet_turtle(body1,4,"red")
            Movement.planet_turtle(body3,4.5,"red")
            Movement.planet_turtle(body4,8,"blue")
            Movement.planet_turtle(body2,2,"white") #moon
            Movement.planet_turtle(body5,10,"orange")
            Movement.planet_turtle(body6,15,"yellow")
            Movement.planet_turtle(body7,13,"brown")
            self.screen.update()
            self.screen.bgcolor("black")

            body1.goto(Movement.big_position(self.li[0],i)) #mercury
            body3.goto(Movement.big_position(self.li[2],-i)) #venus
            
            body4.goto(Movement.big_position(self.li[3],i)) #earth
            body2.goto(Movement.small_position(self.li[1],self.li[3],i)) #moon
            body5.goto(Movement.big_position(self.li[4],i)) #mars
            body6.goto(Movement.big_position(self.li[5],i)) #jupiter
            body7.goto(Movement.big_position(self.li[6],i)) #saturn
            i+=0.1
sun()
ashu=RelativeMotion([[100,4],[20,5],[125,3.2],[160,2.8],[200,2.6],[400,0.52],[500,0.24]])
ashu.around_p1() 
