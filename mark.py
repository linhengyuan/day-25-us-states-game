import turtle

your_score = 0

class MarkMap:
    def __init__(self):
        self.score = 0

# act function: mark on the map, fetch x and y-axis number
    def mark_on_map(self, df):
        row_df = df[df["state"] == self]
        row_list = row_df.values.tolist()[0]
        x_cor = row_list[1]
        y_cor = row_list[2]

        state_object = turtle.Turtle()
        state_object.penup()
        state_object.hideturtle()
        state_object.goto(x_cor, y_cor)
        state_object.write(self, move=False, align='center', font=('Arial', 8, 'normal'))


# while loop, keep the game running until the 50 state finished
while game_is_on:
    ans_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    # Convert ans_state to Title case
    state_list = us_states_df["state"].tolist()

    # Check guess, loop through 50 state
    if ans_state.title() in state_list and ans_state.title() not in right_ans_list:
        right_ans_list.append(ans_state)
        your_score += 1
        print(your_score)

        # Mark the state on the map
        mark_on_map(ans_state)

# if not show empty textinput bar again
# if yes and no repeat, score +1 and show the state on the map
# update the score on the screen text input title
