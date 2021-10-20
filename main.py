from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from pyperclip import copy
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, f"{password}")
    copy(f"{password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    user_website = website_entry.get()
    user_email = email_entry.get()
    user_password = password_entry.get()
    new_data = {
        user_website: {
            "email": user_email,
            "password": user_password,
        }
    }
    if len(user_website) == 0 or len(user_password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode='r') as data_file:
                # Reading old data
                data = json.load(data_file)    # Read json data
        except FileNotFoundError:
            with open("data.json", mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                # Saving the updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD -------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
            print(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

# Windows / Canvas config


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Create labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
# Create entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky=W)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky=W)
email_entry.insert(0, "tory215@gmail.com")
password_entry = Entry(width=29)
password_entry.grid(column=1, row=3, sticky=W)

# Create buttons
gen_password = Button(text="Generate Password", command=generate_password)
gen_password.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", width=10, command=find_password)
search_button.grid(column=2, row=1)
window.mainloop()
