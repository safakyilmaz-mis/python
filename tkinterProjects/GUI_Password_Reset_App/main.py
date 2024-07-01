# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
import json
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip


def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]

    shuffle(password_list)

    gen_password = "".join(password_list)

    password.delete(0, END)
    password.insert(0, gen_password)
    pyperclip.copy(gen_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

# with open as variable
def save():
    new_dic = {
        website.get():
            {
                "email": email.get(),
                "password": password.get(),
            }
    }
    if website.get() == "" or password.get() == "":
        messagebox.showerror("Oops", "Please dont leave any fields empty")
    else:
        try:
            with open("file.json", "r") as file:
                # reading old data
                data = json.load(file)

        except FileNotFoundError:
            with open("file.json", "w") as file:
                json.dump(new_dic, file, indent=4)

        else:
            data.update(new_dic)
            with open("file.json", "w") as file:
                # writing updated data
                json.dump(data, file, indent=4)
        finally:
            website.delete(0, END)
            password.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    try:
        with open("file.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "No data file found")
    else:
        if website.get() in data:
            saved_password = (data[website.get()]["password"])
            pyperclip.copy(saved_password)
            messagebox.showinfo(website.get(),
                                "Email: " + data[website.get()]["email"] + "\n" + "Password: " + data[website.get()][
                                    "password"] + "\n\n" + "Password copied!")
        else:
            messagebox.showerror("Error", "No details for the website exists")


# ---------------------------- UI SETUP ------------------------------- #


windows = Tk()
windows.title("Password Manager")
windows.config(padx=30, pady=40)

canvas = Canvas(width=480, height=200)
Photo = PhotoImage(file="logo.png")
canvas.create_image(240, 100, image=Photo)
canvas.grid(row=1, column=1, columnspan=3)

emailText = Label(text="Website : ", font=("Arial", 15, "bold"), padx=20, pady=5)
emailText.grid(row=2, column=1, sticky="W")

emailText = Label(text="E-mail : ", font=("Arial", 15, "bold"), padx=20, pady=5)
emailText.grid(row=3, column=1, sticky="W")

emailText = Label(text="Password : ", font=("Arial", 15, "bold"), padx=20, pady=5)
emailText.grid(row=4, column=1, sticky="W")

website = Entry(width=20)
website.focus()
website.grid(row=2, column=2, columnspan=2, sticky="W")

email = Entry(width=45)
email.insert(0, "safakyilmaz.g@gmail.com")
email.grid(row=3, column=2, columnspan=2, sticky="W")

password = Entry(width=20)
password.grid(row=4, column=2, sticky="W")

Search = Button(text="Search", font=("Arial", 9), width=16, command=find_password)
Search.grid(row=2, column=3, sticky="W")

Gen_Pass = Button(text="Generate Password", font=("Arial", 9), command=generate_pass)
Gen_Pass.grid(row=4, column=3, sticky="W")

Add = Button(text="Add", font=("Arial", 10, "bold"), width=33, command=save)
Add.grid(row=5, column=2, columnspan=2, pady=10, sticky="W")

windows.mainloop()
