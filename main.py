import turtle 
import pandas as pd
screen = turtle.Screen()
screen.title("U.S. States Game")
img = "D:/projs/py udemy/map game/day-25-us-states-game-start/blank_states_img.gif"
data = pd.read_csv(r"D:\projs\py udemy\map game\day-25-us-states-game-start\50_states.csv")
screen.addshape(img)
turtle.shape(img)


gussed_state = []

all_states = data.state.to_list()

while len(gussed_state)<50:
    answer_state = str(screen.textinput(title=f"{len(gussed_state)}/50 Guess the state",prompt="What's another states's name: ")).title()
    if answer_state in all_states:
        gussed_state.append(answer_state)
        write_turtle = turtle.Turtle()
        write_turtle.hideturtle()
        write_turtle.penup()
        state_data = data[data.state == answer_state]
        write_turtle.goto(state_data.x.item(), state_data.y.item())
        write_turtle.write(state_data.state.item())
    elif answer_state == "None":
        remaining_states = []
        for statess in all_states:
            if statess not in gussed_state:
                remaining_states.append(statess)
        new_data = pd.DataFrame(remaining_states)
        new_data.to_csv("states_to_learn.csv")
        
        break




        

