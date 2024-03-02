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
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    label_timer.config(text="Timer")
    checkmark_label.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    work_sec = WORK_MIN * 60
    if reps % 8 == 0:
        count_timer(long_break_sec)
        label_timer.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_timer(short_break_sec)
        label_timer.config(text="Break", fg=PINK)
    else:
        count_timer(work_sec)
        label_timer.config(text="Work",fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_timer(count):
    count_min = math.floor(count / 60)
    count_sec = (count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0 :
        global timer
        timer = window.after(1000,count_timer,count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔️"
        checkmark_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=202, height=223, bg=YELLOW,highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(102, 111, image=photo)
timer_text = canvas.create_text(102,130,text="00:00", fill="white", font=(FONT_NAME,25,'bold'))
canvas.grid(column=1,row=1)

label_timer = Label(text="Timer",font=(FONT_NAME,35,"bold"),fg=GREEN ,bg=YELLOW)
label_timer.grid(column=1, row=0)

bt_start = Button(text="start",width=10, command=start_timer)
bt_start.grid(column=0, row=2)

bt_reset = Button(text="reset",width = 10,command=reset_timer)
bt_reset.grid(column=2, row=2)

checkmark_label= Label(font=(FONT_NAME,10,"bold"),bg=YELLOW,fg=GREEN)
checkmark_label.grid(column=1, row=3)


window.mainloop()
