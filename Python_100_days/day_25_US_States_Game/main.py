import turtle
import pandas as pd
import os 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# TODO convert the guess to title case
# TODO Check if the guess is among the 50 states
# TODO write correct guesses onto the map
# TODO Use a loop to allow the user to keep guessing
# TODO Record the correct guesses in a list
# TODO Keep track of the score

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", prompt="What's another state's name?").title()
    print(answer_state)


    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        # used list comprehension to shorten above code
        
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

# states_to_learn.csv

# if guessed_states not equal to 50 compare guessed_states to all_states add states that are not in both lists to states_to_learn.csv

# if answer_state is one of the states in the 50_states.csv list
    # if they got it right then it gets printed on the x, y coordinates

# if incorrect reset

print()




screen.exitonclick()