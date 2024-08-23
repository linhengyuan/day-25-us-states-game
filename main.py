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
game_is_on = True

# Fetch data from csv
us_states_df = pandas.read_csv("50_states.csv")

# while loop, keep the game running until the 50 state finished
# while game_is_on:
#     ans_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
#
#     # Convert ans_state to Title case
#     state_list = us_states_df["state"].tolist()
#
#     # Check guess, loop through 50 state
#     if ans_state.title() in state_list and ans_state.title() not in right_ans_list:
#         right_ans_list.append(ans_state.title())
#         your_score += 1
#         print("yes") # act: mark on the map

# if not show empty textinput bar again
# if yes and no repeat, score +1 and show the state on the map
# update the score on the screen text input title

# act function: mark on the map
# fetch x and y-axis number
def mark_on_map(state_reply):
    row_df = us_states_df[us_states_df.state == state_reply]
    for row in row_df.itertuples():
        print(row)


row_list = df.loc[2, :].values.flatten().tolist()

mark_on_map("Alabama")

# Delet this line?
screen.exitonclick()