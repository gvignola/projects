from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

WHITE = "#ffffff"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]

    password_list += [random.choice(symbols) for char in range(random.randint(2, 4))]

    password_list += [random.choice(numbers) for char in range(random.randint(2, 4))]
    random.shuffle(password_list)

    password_new = "".join(password_list)
    # insert inside the entry password
    entry_password.insert(0, password_new)
    # password_n = ""
    # for char in password_list:
    #  password_n += char
    # string to clipboard
    pyperclip.copy(password_new)
    # print(f"Your password is: {password_new}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    webst = entry_web.get()
    em_us = entry_email_usr.get()
    pasw = entry_password.get()
    #webst is the key and it's contain a dict and contains 2 keys
    new_data = {
        webst: {
            "email": em_us,
            "password": pasw,
        }
    }

    if len(webst) == 0 or len(pasw) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any field empty.")
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file) #--> read old data
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)  # n°of spaces to indent all data --> write / save
        else:
            data.update(new_data) # --> update old data with new one
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent= 4) #--> saving

        finally:
            entry_web.delete(0, END)  # delete from start = 0 to end = END
            entry_password.delete(0, END)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = entry_web.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title= "Erro", message= "No Data File Found.")
    else:
        if website in data:
            email = data[website]['email'] #nested dict
            password = data[website]["password"] #nested dict
            messagebox.showinfo(title= website, message= f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title= 'Error', message= f"No details for {website} exist.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Manager")
window.config(pady=50, padx=50)

# canvas
canvas = Canvas(width=200, height=200)

# upload image
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website = Label(text="Website:")
website.grid(row=1, column=0)
email_user = Label(text="Email/Username:")
email_user.grid(row=2, column=0)
password = Label(text="Password:")
password.grid(row=3, column=0)

# entries
entry_web = Entry(width=32)
entry_web.grid(row=1, column=1)
entry_web.focus()  # to put the cursor
entry_email_usr = Entry(width=50)
entry_email_usr.grid(row=2, column=1, columnspan=2)
entry_email_usr.insert(0,
                       "v.giovanni94@icloud.com")  # zero character, or END is a constant which is gonna rapresent the very last
# character that's inside that entry
entry_password = Entry(width=32)
entry_password.grid(row=3, column=1)

# button

gen_pass_button = Button(text="Generate Password", command=generate_pass)
gen_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button  = Button(text= "Search", width= 13, command= find_password)
search_button.grid(row=1, column = 2)

window.mainloop()
