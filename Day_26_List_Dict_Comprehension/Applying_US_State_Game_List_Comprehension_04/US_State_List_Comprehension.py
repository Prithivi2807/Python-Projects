import turtle 
import pandas 

screen=turtle.Screen()
screen.title("U.S State Game")
image = r"C:\Users\Hi\Documents\Python Practice\Day_26_List_Dict_Comprehension\Applying_US_State_Game_List_Comprehension\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv(r"C:\Users\Hi\Documents\Python Practice\Day_26_List_Dict_Comprehension\Applying_US_State_Game_List_Comprehension\50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) != len(all_states):
  answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(all_states)} States Correct", prompt="What's another state's name ?").title()

  if answer_state == "Exit":
    # missing_states = []
    # for state in all_states:
    #   if state not in guessed_states:
    #     missing_states.append(state)
    #     new_data = pandas.DataFrame(missing_states)
    #     print(new_data)
    #     break  """Alterntive  of this 4 line of code"""
    missing_states = [state for state in all_states if state not in guessed_states]
    new_data = pandas.DataFrame(missing_states)
    print(new_data)
    break

  if answer_state in all_states:
    guessed_states.append(answer_state)
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data["state"] == answer_state]
    t.goto(int(state_data["x"].iloc[0]), int(state_data["y"].iloc[0]))
    t.write(answer_state)