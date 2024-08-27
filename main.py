import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Games")
image = "blank_states_img.gif"
# add image into our turtle shape choice
screen.addshape(image)
turtle.shape(image)

# Ans/score storage
right_ans_list = []
your_score = 0

# Fetch data from csv
us_states_df = pandas.read_csv("50_states.csv")

# act function: mark on the map, fetch x and y-axis number
def mark_on_map(state_reply):
    state_data = us_states_df[us_states_df.state == state_reply]
    x_cor = state_data.x.item()
    y_cor = state_data.y.item()

    state_object = turtle.Turtle()
    state_object.penup()
    state_object.hideturtle()
    state_object.goto(x_cor, y_cor)
    state_object.write(state_reply, move=False, align='center', font=('Arial', 8, 'normal'))


# while loop, keep the game running until the 50 state finished
while len(right_ans_list) < 50:
    ans_state = screen.textinput(title=f"{len(right_ans_list)}/50 Guess the State",
                                 prompt="What's another state's name?").title()
    # Convert ans_state to Title case
    state_list = us_states_df["state"].tolist()

    if ans_state.title() == "Exit":
        missing_states = us_states_df["state"].tolist()
        for i in right_ans_list:
            missing_states.remove(i)
        new_df = pandas.DataFrame(missing_states)
        new_df.to_csv("state_to_learn.csv")

        break

    # Check guess, loop through 50 state
    if ans_state.title() in state_list and ans_state.title() not in right_ans_list:
        right_ans_list.append(ans_state)
        your_score += 1
        # Mark the state on the map
        mark_on_map(ans_state)

# states to learn.csv

# for ans in us_states_df[us_states_df.state == state_reply]:
#     if ans not in
#
# data_dict =
#
# df = pandas.DataFrame(data_dict)
