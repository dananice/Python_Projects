from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.back(10)

def move_clockwise():
    tim.right(10)
    tim.forward(10)

def move_counter_clockwise():
    tim.left(10)
    tim.forward(10)

def clear():
    tim.clear()
    tim.up()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="c", fun=clear)
screen.onkey(key="f", fun=move_forward)
screen.onkey(key='b', fun=move_backward)
screen.onkey(key='l', fun=move_counter_clockwise)
screen.onkey(key="r", fun=move_clockwise)
screen.exitonclick()