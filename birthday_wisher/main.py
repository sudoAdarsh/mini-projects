import datetime as dt
import pandas
import random
import smtplib

FROM_EMAIL = "adasrhupadhyay.1234@gmail.com"
PASSWORD = "zhadupkrqcxkqlcm"

df = pandas.read_csv("birthdays.csv")
data_dict = df.to_dict(orient="records")

now = dt.datetime.now()

birthday_sent = False

for entry in data_dict:
    if entry["month"] == now.month and entry["day"] == now.day:
        name = entry["name"]
        email = entry["email"]

        letter_path = random.choice(('letter_1.txt', 'letter_2.txt', 'letter_3.txt', 'letter_4.txt', 'letter_5.txt'))

        with open(f"letter_templates/{letter_path}", encoding="utf-8") as f:
            letter = f.read().replace('[NAME]', name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=FROM_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=FROM_EMAIL,
                to_addrs=email,
                msg=f"Subject:Happy Birthday {name}!\n\n{letter}".encode("utf-8")
            )
        print(f"Today was {name}'s Birthday\nwishes have been sent 😉")
        birthday_sent = True

if not birthday_sent:
    print("Today is nobody's birthday.")
