import turtle

# def get_mouse_click_coor(x, y):
#     print(x,y)

screen = turtle.Screen()
screen.title("US States Game")
image = r"day25\us_states_game\blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

answer_state = screen.textinput(
    title="Guess the State", prompt="What's another State's name?"
)
print(answer_state)

# turtle.onscreenclick(get_mouse_click_coor) -> function to get the states coordinates
# turtle.mainloop()
