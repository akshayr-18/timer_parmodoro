from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICKS=""
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
	global timer
	global TICKS
	global reps
	reps=0
	TICKS=""
	label.config(text="Timer", fg=GREEN,bg=YELLOW, font=(FONT_NAME,40,"bold"))
	label4.config(text="", fg=GREEN,bg=YELLOW, font=(FONT_NAME,20,"normal	"))
	canvas.itemconfig(timer_text,text="00:00")
	window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
	global reps
	global TICKS
	reps+=1
	if reps%8==0:
		label.config(text="BREAK", fg=RED,bg=YELLOW, font=(FONT_NAME,40,"bold"))
		TICKS=""
		label4.config(text=TICKS, fg=GREEN,bg=YELLOW, font=(FONT_NAME,20,"normal	"))
		count_down(LONG_BRAEK_MIN*60)
	elif reps%2==0:
		label.config(text="BREAK", fg=PINK,bg=YELLOW, font=(FONT_NAME,40,"bold"))
		TICKS+="✅"
		label4.config(text=TICKS, fg=GREEN,bg=YELLOW, font=(FONT_NAME,20,"normal	"))
		count_down(SHORT_BRAEK_MIN*60)
	else:
		label.config(text="WORK!!", fg=GREEN,bg=YELLOW, font=(FONT_NAME,40,"bold"))
		count_down(WORK_MIN*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
	global timer
	if count//60<=9 and count//60>=0:
		c_min="0"+str(int(count//60))
	else:
		c_min=int(count//60)
	if count%60<=9 and count%60>=0:
		count_sec="0"+str(int(count%60))
	else:
		count_sec=int(count%60)
	canvas.itemconfig(timer_text,text=f"{c_min}:{count_sec}")
	if count>0:
		timer=window.after(1000,count_down,count-1)
	else:
		start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tom_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tom_img)
timer_text=canvas.create_text(103,130,text="00:00", font=("Courier",24,"normal"),fill="white")
canvas.grid(row=1,column=1)


label=Label(text="Timer", fg=GREEN,bg=YELLOW, font=(FONT_NAME,40,"bold"))
label.grid(row=0,column=1)

button1=Button(text="Start", fg="black",bg=YELLOW, font=(FONT_NAME,15,"normal"),command=start_timer)
button1.grid(row=2,column=0)

button2=Button(text="Reset", fg="black",bg=YELLOW, font=(FONT_NAME,15,"normal"),command=reset)
button2.grid(row=2,column=2)

label4=Label(text=TICKS, fg=GREEN,bg=YELLOW, font=(FONT_NAME,20,"normal	"))
label4.grid(row=3,column=1)





window.mainloop()
