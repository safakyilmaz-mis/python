import tkinter
from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
app_time = None

def reset_timer():
    global reps
    windows.after_cancel(app_time)
    Timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(Timer_text, text="00:00")
    Completed.config(text="")
    reps = 0


def start_timer():
    global reps
    reps += 1
    print(reps)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        Timer.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        Timer.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        Timer.config(text="Work", fg=GREEN)


def count_down(count):
    global reps
    global app_time
    minutes = math.floor(count / 60)
    if minutes < 10:
        minutes = f"0{minutes}"
    second = count % 60
    if second < 10:
        second = f"0{second}"
    canvas.itemconfig(Timer_text, text=f"{minutes}:{second}")
    if count > 0:
        app_time = windows.after(1000, count_down, count - 1)
    if count == 0:
        # print(reps)
        if reps % 2:
            Completed.config(text=int((reps + 1) / 2) * "✔️")
        if reps < 8:
            start_timer()


windows = Tk()
windows.title("Pomodoro App")
windows.config(padx=50, pady=0, bg=YELLOW)

canvas = Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=photo)

Timer_text = canvas.create_text(100, 130, text="00:00", fill="White", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

Timer = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
Timer.config(pady=20)
Timer.grid(row=1, column=2)

Completed = Label(text="", font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW, pady=20, highlightthickness=0)
Completed.grid(row=4, column=2)

Start = Button(text="Start", font=(FONT_NAME, 20, "bold"), bg=YELLOW, highlightthickness=0, command=start_timer)
Start.grid(row=3, column=1)

Reset = Button(text="Reset", font=(FONT_NAME, 20, "bold"), bg=YELLOW, highlightthickness=0, command=reset_timer)
Reset.grid(row=3, column=3)

windows.mainloop()
