import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from turtle_crossing_game.player import STARTING_POSITION

# TODO create turtle
# TODO move turtle
# TODO Create Cars
# TODO move cars randomly along the y axis from right edge to left edge
# TODO when the turtle hits the top edge it levels up & goes back to starting point
# TODO when turtle levels up the car speed increases
# TODO when turtle hits a car game over


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)



player = Player(STARTING_POSITION)
car_manager = CarManager
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    #if player reaches finish line
    if player.player_at_finishline():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.level_up()

    # Detect collision with car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()


