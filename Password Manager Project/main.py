import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list= password_letters+password_numbers+password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    pass_inp.insert(0,password)

    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_inp.get()
    mail=email_inp.get()
    password=pass_inp.get()
    new_data={
        website:{
            "Email":mail,
            "Password":password
        }
    }

    if len(website)==0 or len(mail)==0 or len(password) ==0:
        messagebox.showinfo(title="IMPORTANT!", message="You've left a mandatory field empty!")

    else:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open('data.json','w') as file:
                json.dump(new_data,file,indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            website_inp.delete(0, 'end')
            email_inp.delete(0, 'end')
            pass_inp.delete(0, 'end')
            website_inp.focus()

# ---------------------------- SEARCH ------------------------------- #

def search():
    website = website_inp.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["Email"]
            password = data[website]["Password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_text = Label(text="Website:")
website_text.grid(row=1, column=0)

email_text = Label(text="Email/Username:")
email_text.grid(row=2, column=0)

password_text = Label(text="Password:")
password_text.grid(row=3, column=0)

# Entries
website_inp = Entry(width=32)
website_inp.grid(row=1, column=1, sticky="W")
website_inp.focus()

email_inp = Entry(width=51)
email_inp.grid(row=2, column=1, columnspan=2, sticky="W")

pass_inp = Entry(width=32)
pass_inp.grid(row=3, column=1, sticky="W")

# Buttons
search_button = Button(text="Search", width=14, highlightthickness=0,command=search)
search_button.grid(row=1, column=2, sticky="W")

generate_pass_button = Button(text="Generate Password", width=14, highlightthickness=0,command=generate_pass)
generate_pass_button.grid(row=3, column=2, sticky="W")

add_button = Button(text="Add", width=43,command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="W")

window.mainloop()

