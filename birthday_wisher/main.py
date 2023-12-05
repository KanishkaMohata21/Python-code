import smtplib 
import os
import random
import pandas
from datetime import datetime 

MY_EMAIL="email"
MY_PASSWORD="password"

today=(datetime.now().month,datetime.now().day)

data=pandas.read_csv(r"C:\Users\ssc\Desktop\100.days.of.code\birthday_wisher\birthdays.csv")

birthday_dict={
    (data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()
}

random_letter=random.randint(1,3)
if today in birthday_dict:
    birthday_person=birthday_dict[today]
    file_path=r"C:\Users\ssc\Desktop\100.days.of.code\birthday_wisher\letter_templates"
    file = os.path.join(file_path, f"letter_{random_letter}.txt")
    with open(file) as letter_file:
        contents=letter_file.read()
        contents=contents.replace("[NAME]",birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=birthday_person["email"],msg=f"Subject:HAPPY BIRTHDAY!\n\n{contents}")