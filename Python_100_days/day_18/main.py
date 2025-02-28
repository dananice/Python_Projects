import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
# for random color you have to change the color mode in the module
turtle.colormode(255)
tim.shape("turtle")
tim.color("purple")

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# made a straight dotted line 
for _ in range(15):
    tim.forward(10)
    tim.up(10)
    tim.forward(10)
    
    
# made a dotted square
for i in range(4):
    tim.right(90)
    for _ in range(17):
        tim.forward(10)
        tim.up()
        tim.forward(10)
        tim.down(10)    
    
# make different shapes and change color
colors = ["dark orange", "magenta", "dark orchid","gold", "green", "crimson", "blue", "midnight blue","black" ]

def shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    shapes(shape_side_n)

# Random walk
directions = [0, 90, 180, 270] 
tim.pensize(10)
tim.speed("fastest")

for i in range(100):
    tim.color(random.choice(colors))
    tim.forward(25)
    tim.setheading(random.choice(directions))

# to make the color change random
# tim.color(random.choice(colors)) change to tim.color(random_color())
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255) 
    random_color = (r, g,b)
    return random_color

# for the below spirograph I commented out pensize, directions, other for loops changed speed to fastest 
 
def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
        
draw_spirograph(5)        
     
 
screen =  Screen()
screen.exitonclick()
    