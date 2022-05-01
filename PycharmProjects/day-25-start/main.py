from turtle import Turtle, Screen
import pandas
screen = Screen()
tom = Turtle()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
tom.shape(image)
data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 Guess the State',
                                    prompt="What's another state's name?").title()

    if answer_state in all_states:
        t = Turtle()
        t.ht()
        t.up()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        guessed_states.append(answer_state)
    if answer_state == 'Off':
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break

# guessed_states 'states_to_learn.csv'