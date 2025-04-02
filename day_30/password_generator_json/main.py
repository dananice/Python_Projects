from tkinter import *
from tkinter import messagebox, END  # popup messagebox 
import os
from random import choice, randint, shuffle
import pyperclip # module to copy input to clipboard
import json

os.chdir(os.path.dirname(os.path.abspath(__file__)))

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
# created a json dictionary new_data  json dump writes to json file, indent makes easier to read
def save():

    website= website_input.get()
    email = email_username_input.get()
    password = password_input.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
            
        }
    }
    
                
    if len(website) == 0 or len(password)  == 0:
        messagebox.showinfo(title="Oops", message="Please fill in all fields.")
    else:
        try:
            with open("data.json", "r") as data_file: # use "w" with json.dump, "r" with json.load & print stmt,"w" with update
                #json.dump(new_data, data_file, indent=4 )  #(dict name, file name to save to, indent makes eaier to read)
                # Reading old data
                try:
                    data = json.load(data_file)  # changes to a python dict  (load reads a file  loads convert to python dict)
                except json.JSONDecodeError:
                        # Handle the case where the file is empty or contains invalid JSON
                        data = {}  # Initialize an empty dictionary
        except FileNotFoundError:
            data = {}  # Initialize an empty dictionary if the file doesn't exist

        data.update(new_data)  # Update or add the new data
             
        with open("data.json", "w") as data_file:   
            # Saving updated data
            json.dump(data, data_file, indent=4 ) # to update use load, update, then dump note file change in dump
                
                
        website_input.delete(0,END)
        password_input.delete(0,END)
            
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:  
        messagebox.showinfo(title="Error", message="No Data File Found.")     
    else:    
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:        
            messagebox.showinfo(title="Error", message=f"No Details for {website} exists.")

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
website_input = Entry(width=26,)
website_input.grid(column=1, row=1)
website_input.focus()    # puts cursor in textbox

email_username_input = Entry(width=44)
email_username_input.grid(column=1, columnspan=2, row=2)
email_username_input.insert(0, "dana@gmail.com")

password_input = Entry( width=26)
password_input.grid(column=1, row=3)

# Button
# command calls the function
search_button = Button(text="Search", bg="white", width=13, command=find_password)
search_button.grid(column=2, row=1,)
generate_password_button = Button(text="Generate Password", bg="white", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", bg="white", width=38, command=save)
add_button.grid(column=1, columnspan=2, row=4)

window.mainloop()