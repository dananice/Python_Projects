from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#1aa13c"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmarks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    # If it's the 2nd/4th/6th rep:
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
#     If it's the 1st/3rd/5th/7th rep:
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# timer countdown 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")   # changes time format to 00:00
    if count > 0:
        global timer
        timer = window.after(1080, count_down, count -1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)   # loop for the work sessions to add the checkmark 
        for _ in range(work_sessions):
            mark += "✅"
        checkmarks.config(text=mark)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



timer_label = Label(text="Timer", fg=GREEN,bg=YELLOW, font=(FONT_NAME,35))
timer_label.grid(column=1, row=0)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)  # x & y are required
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


reset_button = Button(text="Reset", font=(FONT_NAME, 18), command=reset_timer)
reset_button.grid(column=2, row=2)

start_button = Button(text="Start", font=(FONT_NAME, 18), command=start_timer)
start_button.grid(column=0, row=2)

checkmarks = Label(fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=3)





window.mainloop()
