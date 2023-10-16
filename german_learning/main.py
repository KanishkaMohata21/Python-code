from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
Current_card={}
to_learn={}
try:
    data=pandas.read_csv(r"C:\Users\ssc\Desktop\100.days.of.code\german\words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv(r"C:\Users\ssc\Desktop\100.days.of.code\german\data.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")


def is_known():
    to_learn.remove(Current_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv(r"C:\Users\ssc\Desktop\100.days.of.code\german\words_to_learn.csv",index=False)
    next_card()

def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=Current_card["english"],fill="white")
    canvas.itemconfig(card_background,image=card_back_img)

def next_card():
    global Current_card,flip_timer
    window.after_cancel(flip_timer)
    Current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="German")
    canvas.itemconfig(card_title,text="German",fill="black")
    canvas.itemconfig(card_word,text=Current_card["german"],fill="black")
    canvas.itemconfig(card_background,image=card_front_img)
    flip_timer=window.after(5000,func=flip_card)

window=Tk()
window.title("LEARN")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(5000,func=flip_card)

canvas=Canvas(width=800,height=526)
card_back_img=PhotoImage(file=r"C:\Users\ssc\Desktop\100.days.of.code\german\images\card_back.png")
card_front_img=PhotoImage(file=r"C:\Users\ssc\Desktop\100.days.of.code\german\images\card_front.png")
card_background=canvas.create_image(400,263,image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_title=canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263,text="word",font=("Ariel",40,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

cross_image=PhotoImage(file=r"C:\Users\ssc\Desktop\100.days.of.code\german\images\wrong.png")
unknown_button=Button(image=cross_image,highlightthickness=0,command=is_known)
unknown_button.grid(row=1,column=0,)

check_image=PhotoImage(file=r"C:\Users\ssc\Desktop\100.days.of.code\german\images\right.png")
known_button=Button(image=check_image,highlightthickness=0,command=next_card)
known_button.grid(row=1,column=1)

next_card()

window.mainloop()