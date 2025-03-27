from tkinter import *
from tkinter import messagebox  # popup messagebox 
from random import choice, randint, shuffle
import pyperclip # module to copy input to clipboard

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# condensed version of day 5 password generator using list comprehension instead of for loops
# list comprehension [new_item for item in range()]

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# picks 8 - 10 random letters, 2-4 random symbols and numbers
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)


    password = "".join(password_list)  # joins the password letters numbers & symbol together
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website= website_input.get()
    email = email_username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password)  == 0:
        messagebox.showinfo(title="Oops", message="Please fill in all fields.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\n Password: {password} \n Is it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0,END)
                password_input.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=70, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img =PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)  # must include x & y position
canvas.grid(column=1, row=0)

# Label
website_label = Label(text="Website: ", bg="white")
website_label.grid(column=0, row=1)
email_username_label = Label(text="Email/Username: ", bg="white")
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password: ", bg="white")
password_label.grid(column=0, row=3)

# Entry
website_input = Entry(width=40,)
website_input.grid(column=1, columnspan=2, row=1)
website_label.focus()    # puts cursor in textbox

email_username_input = Entry(width=40)
email_username_input.grid(column=1, columnspan=2, row=2)
email_username_input.insert(0, "dana@gmail.com")

password_input = Entry( width=22)
password_input.grid(column=1, row=3)

# Button
# command calls the function
generate_password_button = Button(text="Generate Password", bg="white", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", bg="white", width=34, command=save)
add_button.grid(column=1, columnspan=2, row=4)

window.mainloop()