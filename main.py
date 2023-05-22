import pandas as pd
import turtle

all_states = pd.read_csv('50_states.csv')
print(all_states)
guessed_states = []
screen = turtle.Screen()
screen.title("US States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

state_list = all_states.state.to_list()
while len(guessed_states) < 50:

    answer_state = (screen.textinput(prompt="Please guess a name of a state",
                                     title=f"{len(guessed_states)}/50 states guessed")).capitalize()

    if answer_state == "Exit":
        missing_state = [state for state in state_list if state not in guessed_states]
        missing_state_data = pd.DataFrame(missing_state)
        missing_state_data.to_csv("states_to_learn.csv")

        break


    if answer_state in state_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = all_states[all_states.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


screen.exitonclick()

