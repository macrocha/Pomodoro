from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    # this function is used to reset timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    # this function is used to start the timer

    # increase reps everytime timer is done
    global reps
    reps += 1

    # convert the working time, short, and long
    # breaks into seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # if a rep is divisible by 8, long break
    if reps % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text="Long break", fg=RED)
    # if a rep is even, short break
    elif reps % 2 == 0:
        countdown(short_break_sec)
        title_label.config(text="Short break", fg=PINK)
    # otherwise, it is a working time
    else:
        countdown(work_sec)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    # this function takes in a number to countdown from
    # and the number is updated in timer_text

    # variables converting count to
    # nearest minute and remaining seconds
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # have a zero display when getting to single digits for seconds
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # update timer text in the format "minutes:seconds"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    # counts down as long as the count > 0
    if count > 0:
        # executes a command after a time delay
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        # adds a checkmark everytime a work session is complete
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #


# create window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# create a label for timer and checkmark
title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
title_label.grid(column=1, row=0)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

# create canvas and add image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

# create text in the middle of the tomato
timer_text = canvas.create_text(100, 125, text='00:00', fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# create start and reset buttons
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()