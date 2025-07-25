from tkinter import * 
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

  # Password Generator Project
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
              'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 
              'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
              'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  ### nr_letters, nr_symbols, nr_numbers in that given list

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

  if len(website) == 0 or len(password) == 0 or len(email) == 0:
    messagebox.showinfo(title=website, message=f"Please don't leave any field empty!")
  else:
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                           f"\nPassword: {password} \nIs it ok to save ?")
    # messagebox.showinfo(title="Title", message="Message")

    if is_ok:
      with open(r"C:\Users\Hi\Documents\Python_Practice\Day_29_Password_Manager\data_1.txt", "a") as datafile:
        datafile.write(f"{website} | {email} | {password} \n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file = r"C:\Users\Hi\Documents\Python_Practice\Day_29_Password_Manager\logo.png")
canvas.create_image(100, 100, image=logo_img) # w & h = 200 so x & y half of the size 100
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

Email_label = Label(text="Email/Username: ")
Email_label.grid(column=0, row=2)

Password_label = Label(text="Password: ")
Password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

Email_entry = Entry(width=35)
Email_entry.grid(column=1, row=2, columnspan=2)
Email_entry.insert(0, "Prithivi007@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, columnspan=2)

# Buttons 
Gen_password_button = Button(text="Generate Password", command=generate_password)
Gen_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()