import pandas as pd
import turtle

# Setup the screen to show the US map
screen = turtle.Screen()
screen.title("Can you guess all the US States")
screen.bgcolor("black")
screen.setup(width=695, height=505)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Create the turtle that will write the state names on the map
write_state = turtle.Turtle()
write_state.speed("fastest")
write_state.color("black")
write_state.ht()
write_state.pu()

# Reads the US states and turns the DataFrame to a list
data = pd.read_csv("50_states.csv")
states = data.state.to_list()

correct_answers = 0
correct_guesses = []

# Keeps the game going until Exit is entered or all the states have been guessed
while correct_answers < 50:
    answer = screen.textinput(title=f"{correct_answers}/50 States guessed", prompt="Name a State").title()
    if answer == "Exit":
        break
    if answer in states and answer not in correct_guesses:
        correct_answers += 1
        correct_guesses.append(answer)
        cur_state = data[data.state == answer]
        write_state.goto(int(cur_state.x), int(cur_state.y))
        write_state.write(answer, font=("Arial", 7, "normal"), align="center")

# Creates a list of the states that weren't guessed
missed_states = [state for state in states if state not in correct_guesses]

# Adds the states that were missed to a csv file
df = pd.DataFrame(missed_states)
# noinspection PyTypeChecker
df.to_csv("states_to_learn.csv")
