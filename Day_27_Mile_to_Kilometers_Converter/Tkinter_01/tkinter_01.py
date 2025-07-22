from tkinter import * 

def button_clicked():
  print("I got Clicked")
  new_text = input.get()
  my_label.config(text= new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width= 500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text = "I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack(expand=True)  # It packed in center of the program
# my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
# In the comman don't need to call the method put the method name
button = Button(text = "Click Me", command=button_clicked)  
button.grid(column=1, row=1)

# # New button
new_button = Button(text= "New Button", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)





window.mainloop()
