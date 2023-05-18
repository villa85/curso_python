import turtle             # allows us to use the turtles library
wn = turtle.Screen()      # creates a graphics window
alex = turtle.Turtle()    # create a turtle named alex
alex.forward(150)         # tell alex to move forward by 150 units
alex.left(90)             # turn by 90 degrees
alex.forward(75)          # complete the second side of a rectangle
alex.left(90)
alex.forward(150)
alex.left(90)
alex.forward(75)

alex.clear()
distance = 50
angle = 90
for _ in range(10):
    turtle.forward(distance)
    turtle.right(angle)
    distance = distance + 10
    angle = angle - 3

# import turtle library

import turtle
colors = [ "red","purple","blue","green","orange","yellow"]
my_pen = turtle.Pen()
turtle.bgcolor("black")
for x in range(360):
    my_pen.pencolor(colors[x % 6])  # % Residuo
    my_pen.width(x/100 + 1)
    my_pen.forward(x)
    my_pen.left(59)
wn.exitonclick()

