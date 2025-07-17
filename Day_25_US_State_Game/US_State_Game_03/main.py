import turtle 
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = r"C:\Users\Hi\Documents\Python Practice\Day_25_US_State_Game\US_State_Game_03\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# ##get the state names by using the maps
# def get_mouse_click_coord(x, y):
#   print(x, y)
# turtle.onscreenclick(get_mouse_click_coord)
# turtle.mainloop() # alternative for scressn.exitonclick it will run continously

data = pandas.read_csv(r"C:\Users\Hi\Documents\Python Practice\Day_25_US_State_Game\US_State_Game_03\50_states.csv")
# print(data)
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) != len(all_states):
  answer_state = screen.textinput(title=f"{len(guessed_states)}/ {len(all_states)} States Correct", prompt="what's another state's name ?").title()

  if answer_state == "Exit":
    missing_state = []
    for state in all_states:
      if state not in guessed_states:
        missing_state.append(state)
    new_data = pandas.DataFrame(missing_state)
    # new_data.to_csv("states_to_learn.csv")
    new_data.to_csv(r"C:\Users\Hi\Documents\Python Practice\Day_25_US_State_Game\US_State_Game_03\states_to_learn.csv")
    break

  if answer_state in all_states:
    guessed_states.append(answer_state)
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data["state"] == answer_state]
    t.goto(int(state_data["x"].iloc[0]), int(state_data["y"].iloc[0]))
    t.write(answer_state)

