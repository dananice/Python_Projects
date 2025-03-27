from tkinter import *


# todo create window
# todo create label
# todo create buttons
# todo create input
# todo calculate miles to km

    

def calculate_km():
    miles = float(miles_input.get())
    km = 1.60934 * miles
    km_result_label.config(text=f"{km}")
    return km
# window

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=50, pady=50)

# Label
is_equal_to_label = Label(text= "is equal to ", font=("Arial",18))
is_equal_to_label.grid(column=0, row=1)

km_label = Label(text="Km", font=("Arial",18))
km_label.grid(column=3, row=1)

km_result_label = Label(text="0", font=("Arial", 18))
km_result_label.grid(column=2, row=1)

mile_label = Label(text="Miles", font=("Arial", 18))
mile_label.grid(column=3, row=0)

# button
calculate_button = Button(text="Calculate",font=("Arial",18), command=calculate_km)
calculate_button.grid(column=2, row=2)

# Entry
miles_input = Entry(width=7, font=("Arial, 18") )
miles_input.grid(column=2, row= 0)



window.mainloop()