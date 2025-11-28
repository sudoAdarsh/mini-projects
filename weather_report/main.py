import requests
import os
import smtplib
from datetime import datetime
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv(dotenv_path="../.env")

FROM_EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")
api_key = os.getenv("OPENWEATHER_API")
account_sid = os.getenv("TWILIO_ACC_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
reciever_number = os.getenv("PHONE_NUM")

def send_sms(msg):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=msg,
        from_="+18624076660",
        to=reciever_number,
    )
    print(message.status)

def send_mail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:Weather Report\n\n{forecast_report}".encode("utf-8")
        )
    print("Mail Sent")

url = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat" : 19.19,   # 19.19
    "lon" : 73.22,   # 73.22
    "cnt" : 5,
    "appid" : api_key
}

response = requests.get(url, params=parameters)
response.raise_for_status()
data = response.json()

weather_data = []
will_rain = False

for hour_data in data['list']:
    hourly_data = hour_data['weather'][0]
    time = hour_data["dt_txt"]
    weather_data.append({time : hourly_data['description']})
    condition_code = hourly_data['id']
    if int(condition_code) < 700:
        will_rain = True


current_date = datetime.now().strftime("%B %d, %Y")
forecast_report = f"{data['city']['name']}'s weather forecast for {current_date}\n\n"

for entry in weather_data:
    for time, condition in entry.items():
        forecast_report += (f"{time} : {condition}\n")

send_mail()
if will_rain:
    send_sms(msg="It's Raining today, don't forget your ☂️")
else:
    send_sms(msg="Looks like clear skies today, have a great day! 🌤️")
