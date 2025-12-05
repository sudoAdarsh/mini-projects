from dotenv import load_dotenv
import os
import pandas
import smtplib

load_dotenv(dotenv_path="/home/adarshu/Documents/Coding/Python/mini-projects/.env")

FROM_EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")        # Note: You have to create a app password for your mail id
TO_EMAIL = os.getenv("TO_EMAIL")

def send_mail(msg):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs=TO_EMAIL, 
            msg=msg.encode("utf-8")
        )
        print("coding_quotes run completed")

df = pandas.read_json("coding_quotes/quotes.json")

quotes = df[df["rating"] >= 4.5]

quote = quotes.sample().iloc[0]
message = f"Subject:Hey Coder!\n\n{quote.author} once said,\n{quote.text}"
send_mail(message)