from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    # my_label.config(text="Button Got Clicked")  # changes text
    my_label.config(text=new_text)

# window

window = Tk()
window.title("My First GUI Program") 
window.minsize(width=500, height=300)
window.config(padx=128, pady=128)  # adds padding to the window 

# Label

my_label = Label(text = "I Am a Label", font=("Arial", 24, "bold" ))
my_label["text"] = "New Text"
my_label.config(text="New Text")
# my_label.pack()  #places on the screen can only use left right top bottom
# my_label.place(x=100, y=100) #places at specific point on screen 
my_label.grid(column=0, row=0)

# Button

button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="New_ Button")
new_button.grid(column=2, row=0)


# Entry

input = Entry(width=10)
print(input.get()) # get returns entry as a string
# input.pack() # can't use pack with grid
input.grid(column=3, row=2)













window.mainloop()
