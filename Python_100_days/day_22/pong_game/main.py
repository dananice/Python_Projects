from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# TODO Create the screen
# TODO Create and move a paddle
# TODO Create another paddle
# TODO Create the ball and make it move
# TODO Detect collision with wall and bounce
# TODO Detect collision with paddle
# TODO Detect when paddle misses
# TODO Keep score

# Create the Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.title("PONG")
screen.bgcolor("black")
screen.tracer(0)  # makes paddles and ball show at one time

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "e")
screen.onkey(l_paddle.go_down, "d")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()    # here for the tracer but kept in code just in case
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    # Detect if r paddle misses
    if ball.xcor()  > 280:
        ball.reset_position()
        scoreboard.l_point()

    # detect if l paddle misses
    if ball.xcor()< -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()