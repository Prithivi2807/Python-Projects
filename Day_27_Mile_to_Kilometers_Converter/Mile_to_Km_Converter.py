from tkinter import * 

def miles_to_km():
  miles = (float(miles_input.get()))
  # print(type(miles))
  Km = round((miles * 1.609344),2)
  kilometer_result_label.config(text=f"{Km}")

window = Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)

miles_input = Entry()
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="Is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="KM")
kilometer_label.grid(column=2, row=1)

calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(column=1, row=2)



window.mainloop()