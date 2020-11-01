#import turtle
import turtle
from random import randint
 
window = turtle.Screen()
turtle.bgcolor("black")
turtle.color("yellow")
turtle.speed(0)

#code to draw a single star
def draw_star():
    turns = 5
    turtle.begin_fill()
    while turns>0:
        turtle.forward(25)
        turtle.left(145)
        turns = turns - 1
    turtle.end_fill()

#code to draw 100 stars
num_stars = 0
while num_stars<100:
    x = randint(-300, 300)
    y = randint(-300, 300)
    draw_star()
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    num_stars = num_stars +1

windows.exitonclick()
    
 
