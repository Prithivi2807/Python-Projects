from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip 
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
  
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 
            'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
            'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  password_letters = [choice(letters) for _ in range(randint(8, 10))]
  password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
  password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

  password_list = password_letters + password_symbols + password_numbers
  shuffle(password_list)
  
  password = "".join(password_list)
  # print(f"Your password is: {password}")
  password_entry.insert(0, password)
  pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
  website = website_entry.get()
  email = Email_entry.get()
  password = password_entry.get()
  new_data = {
    website:{
      "email":email,
      "password": password,
    }
  }

  if len(website) == 0 or len(password) == 0:
    messagebox.showinfo(title=website, message=f"Please don't leave the field empty! ")
  else:
      try:
        with open(r"C:\Users\Hi\Documents\Python_Practice\Day_30_Errors_Exception_Json_Data_Improving\Password_Manager_06\data.json", mode="r") as data_file:
            # Reading old data
            data = json.load(data_file)

      except FileNotFoundError:
          with open(r"C:\Users\Hi\Documents\Python_Practice\Day_30_Errors_Exception_Json_Data_Improving\Password_Manager_06\data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
            
      else:
          # Updating old data with new data
          data.update(new_data)

          with open(r"C:\Users\Hi\Documents\Python_Practice\Day_30_Errors_Exception_Json_Data_Improving\Password_Manager_06\data.json", mode="w") as data_file:
            # Saving updated data
            json.dump(data, data_file, indent=4)
          
      finally:
          website_entry.delete(0, END)
          password_entry.delete(0, END)

# ---------------------------- Find Password ------------------------------- #
def find_password():
  website = website_entry.get()
  try:
    with open(r"C:\Users\Hi\Documents\Python_Practice\Day_30_Errors_Exception_Json_Data_Improving\Password_Manager_06\data.json") as data_file:
        data = json.load(data_file)
  except FileNotFoundError:
    messagebox.showinfo(title="Error", message=f"No Data file Found")
  else:
    if website in data:
      email = data[website]["email"]
      password = data[website]["password"]
      messagebox.showinfo(title=website, message=f"Email: {email} \n Password: {password}")
    else:
      messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
 


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file=r"C:\Users\Hi\Documents\Python_Practice\Day_29_Password_Manager\logo.png")
canvas.create_image(100, 100, image=logo_img) 
canvas.grid(column=1, row=0, pady=20)
# canvas.grid(column=1, row=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="w")

Email_label = Label(text="Email/Username: ")
Email_label.grid(column=0, row=2, sticky="w")

Password_label = Label(text="Password: ")
Password_label.grid(column=0, row=3, sticky="w")

# Entries
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, columnspan=1, sticky="w")
website_entry.focus()

Email_entry = Entry(width=35)
Email_entry.grid(column=1, row=2, columnspan=1, sticky="w")
Email_entry.insert(0, "prithivi2807@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, columnspan=1, sticky="w")

# Buttons
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1, columnspan=1)

Gen_password_button = Button(text="Generate Password", command=generate_password)
Gen_password_button.grid(column=2, row=3, columnspan=1)

add_button = Button(text="Add", width= 36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()