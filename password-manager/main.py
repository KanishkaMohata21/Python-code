from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for i in range(randint(8, 10))]
    password_symbols = [choice(symbols) for i in range(randint(2, 4))]
    password_numbers = [choice(numbers) for i in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data={
        website:{
            "email":email,
            "password":password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "f"\nPassword: {password} \nIs it ok to save?")
    
    if is_ok:
        try:
            with open(r"C:\Users\ssc\Desktop\100.days.of.code\password-manager-start\data.json","r") as data_file:
                data=json.load(data_file)
        except FileNotFoundError:
            with open(r"C:\Users\ssc\Desktop\100.days.of.code\password-manager-start\data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)
            with open(r"C:\Users\ssc\Desktop\100.days.of.code\password-manager-start\data.json","w") as data_file:
                json.dump(data,data_file,indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)

def find_password():
    website=website_entry.get()
    try:
        with open (r"C:\Users\ssc\Desktop\100.days.of.code\password-manager-start\data.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error",message="No data file found")
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email:{email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {website} exists")

window=Tk()
window.title("PASSWORD MANAGER")
window.config(padx=50,pady=50)

canvas=Canvas(height=200,width=200)
logo_img=PhotoImage(file=r"C:\Users\ssc\Desktop\100.days.of.code\password-manager-start\logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

website_label=Label(text="WEBSITE:")
website_label.grid(row=1,column=0)

email_label=Label(text="EMAIL/USERNAME:")
email_label.grid(row=2,column=0)

password_label=Label(text="PASSWORD:")
password_label.grid(row=3,column=0,)

website_entry=Entry(width=32)
website_entry.grid(row=1,column=1)
website_entry.focus()

email_entry=Entry(width=55)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"kanishkamohta@gmail.com")

password_entry=Entry(width=32)
password_entry.grid(row=3,column=1)

generate_password_button=Button(text="GENERATE PASSWORD",command=generate_password)
generate_password_button.grid(row=3,column=2)

search_button=Button(text="Search",width=13,command=find_password )
search_button.grid(row=1,column=2)

add_button=Button(text="ADD",width=25,command=save)
add_button.grid(row=4,column=1)
window.mainloop()


