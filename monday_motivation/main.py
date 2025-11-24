import datetime as dt
import smtplib
import random

FROM_EMAIL = "your_mail"
PASSWORD = "your_app_password"        # Note: You have to create a app password for your mail id
TO_EMAIL = "reciever's_mail"

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