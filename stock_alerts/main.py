import requests
import os
import smtplib
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
FROM_EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")
stock_api_key = os.getenv("ALPHAVANTAGE_API")
news_api_key = os.getenv("NEWS_API")


def send_mail(msg):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:Stock Update!\n\n{msg}".encode("utf-8")
        )
    print("Mail Sent")


stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : stock_api_key
}

news_params = {
    "q" : "Tesla",
    "apiKey" : news_api_key
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

daily_values = [value for (key, value) in data.items()]

yesterday_closing_price = float(daily_values[0]['4. close'])
day_before_yesterday_closing_price = float(daily_values[1]['4. close'])


percentage_diff = round((abs(yesterday_closing_price - day_before_yesterday_closing_price) / ((yesterday_closing_price + day_before_yesterday_closing_price) / 2)) * 100, 2)

message_sent = False

if percentage_diff >= 3:
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = response.json()['articles'][:3]
    content = []
    for item in articles:
        content.append(f"Headline: {item['title']}\nBrief: {item['description']}")

    if (yesterday_closing_price - day_before_yesterday_closing_price) < 0:
        message = f"TSLA: 🔻{percentage_diff}%\n\n"
        for i in range (3):
            message += f"{content[i]}\n\n"
        send_mail(msg=message)
        message_sent = True
    else:
        message = f"TSLA: 🔺{percentage_diff}%\n\n"
        for i in range (3):
            message += f"{content[i]}\n\n"
        send_mail(msg=message)
        message_sent = True


if not message_sent:
    print("No mail was sent")

