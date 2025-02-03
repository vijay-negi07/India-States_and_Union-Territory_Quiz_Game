import turtle
import pandas

screen = turtle.Screen()
screen.title("India States Game")
image = "india.gif"

screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("india_states.csv")
all_states = data.state.to_list() #converting the state column in the 50 sates.csv file into list.

guessed_states = []
while len(guessed_states) < 37:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/37 States and Union Territories Correct", prompt="What's another State's name or Union Territory's name ? ").title()  #title() used to convert lower word of 1st letter to capital.
    
    if answer_state == "Exit":
        missing_states = [] #make a list of states that the user has not answer. or unable to answer.
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break

    if answer_state in all_states:    # this part of the program to locate the name given by the user in the map.
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup( )
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state,font=("Albertus Extra Bold ",10,"normal","bold"))


