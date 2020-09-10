import turtle


raf= turtle.Turtle()
raf.getscreen().bgcolor("cyan")
raf.speed(200)
raf.color("red")
raf.pensize(2)
raf.penup()
raf.goto((-200, 0))
raf.pendown()

def star (turtle, size):
	if size<= 10:
		return
	else :
		turtle.begin_fill()
		for i in range(5):
			turtle.fd(size)
			star(turtle, size/3)
			turtle.lt(216)
	turtle.end_fill()

star(raf, 300)



turtle.exitonclick()


import turtle 
import math 

raf= turtle.Turtle()
raf.speed(0)
raf.getscreen().bgcolor('black')
raf.pensize(2)
raf.hideturtle()

for i in range (9):
	for colours in ('red','orange', 'blue', 'magenta', 'cyan', 'purple', 'yellow', 'white', 'green'):
		raf.color(colours)
		raf.circle(100)
		raf.lt(5)



raf.exitonclick()
