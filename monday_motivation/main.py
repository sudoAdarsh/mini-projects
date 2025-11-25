from dotenv import load_dotenv
import os
import datetime as dt
import smtplib
import random


load_dotenv(dotenv_path="../.env")

FROM_EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")        # Note: You have to create a app password for your mail id
TO_EMAIL = os.getenv("TO_EMAIL")

def send_mail():

    with open("quotes.txt") as quotes_data:
        data = quotes_data.readlines()
        quote = random.choice(data)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs=TO_EMAIL, 
            msg=f"Subject:Monday motivation\n\n{quote}"
        )


day = dt.datetime.now().weekday()




send_mail() if day == 0 else print("Today is not Monday\nNo Motivation for today")