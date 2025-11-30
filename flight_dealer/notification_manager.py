import os 
import smtplib
from dotenv import load_dotenv

load_dotenv(dotenv_path="/home/adarshu/Documents/Coding/Python/mini-projects/.env")

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

class NotificationManager:
    def __init__(self):
        self.EMAIL = os.getenv("EMAIL")
        self.PASSWORD = os.getenv("PASSWORD")
        self.TO_EMAIL = os.getenv("TO_EMAIL")
    
    def send_mail(self, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.EMAIL, password=self.PASSWORD)
            connection.sendmail(
                from_addr=self.EMAIL,
                to_addrs=self.TO_EMAIL,
                msg=message
            )
        print("Flight details sent Succesfully.")