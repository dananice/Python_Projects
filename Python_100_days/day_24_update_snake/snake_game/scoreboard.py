from turtle import Turtle
import csv
import os  # set cwd as (current working directory) same folder as python file

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.csv") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.csv", "w") as data:
                data.write(f"{self.high_score}")      
        self.score = 0
        self.update_scoreboard()      


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)