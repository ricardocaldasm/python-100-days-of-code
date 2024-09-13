import turtle
import pandas

# def get_mouse_click_coor(x, y):
#     print(x,y)

screen = turtle.Screen()
screen.title("US States Game")
image = r"day25\us_states_game\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv(r"day25\us_states_game\50_states.csv")
all_states = data.state.to_list()  # or data["state"]
guessed_states = list()

while len(guessed_states) < 50:
    answer_state = (
        screen.textinput(
            title=f"{len(guessed_states)}/50", prompt="What's another state's name?"
        )
        .strip()
        .title()
    )

    # if answer_state == "Exit".title():
    #     missing_states = list()
    #     for state in all_states:
    #         if state not in guessed_states:
    #             missing_states.append(state)
    if answer_state == "Exit".title():
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv(r"day25\us_states_game\states to learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_name_pos = turtle.Turtle()
        state_name_pos.hideturtle()
        state_name_pos.penup()
        state_data = data[data.state == answer_state]
        state_name_pos.goto(state_data.x.item(), state_data.y.item())
        # .item() get only the value of the line, not showing the line number
        state_name_pos.write(state_data.state.item())  # or answer_state

# generate a new file - states_to_learn.csv


# turtle.onscreenclick(get_mouse_click_coor) -> function to get the states coordinates
# turtle.mainloop()

# TODO if answer_state is one of the states in all the states of the 50_states.csv
# if right:
# create a turtle to write the name of the state at the state's x and y coordinate
