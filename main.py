import turtle

screen = turtle.Screen()
screen.title("US States Games")
image = "blank_states_img.gif"
# add image into our turtle shape choice
screen.addshape(image)
turtle.shape(image)

ans_state = screen.textinput(title="Guess the State", prompt="What is the another state's name")
print(ans_state)

#


# should I need this line?
screen.exitonclick()