from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import smtplib
import os
import time

load_dotenv(dotenv_path="/home/adarshu/Documents/Coding/Python/mini-projects/.env")

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

TARGET_PRICE = 1100


def send_mail():
    for attempt in range(5):
        try:
            with smtplib.SMTP("smtp.gmail.com", timeout=10) as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=TO_EMAIL,
                    msg=f"Subject:Price drop Alert! \n\nPigeon 1800 W Induction Cooktop Push Button (Black, Favourite) GET IT ONLY FOR {price}Rs.\n{url}".encode("utf-8")
                )
            print("mail report sent, run completed")
            return
        except Exception as e:
            print(f"Email failed, retrying {attempt+1}/5", e)
            time.sleep(3)
    print("Email completely failed after retries")




headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:145.0) Gecko/20100101 Firefox/145.0",
    "Accept-Language": "en-US"
    }

url = "https://www.flipkart.com/pigeon-1800-w-induction-cooktop-push-button/p/itm3893130ae5422?pid=ICTDZZM3SKDMH5CK&lid=LSTICTDZZM3SKDMH5CKG5CZSW&marketplace=FLIPKART&q=induction+stove&store=j9e%2Fm38%2F575&spotlightTagId=default_FkPickId_j9e%2Fm38%2F575&srno=s_1_3&otracker=search&otracker1=search&fm=Search&iid=ba2d077b-8d98-4f9c-8fb7-e64333ef454f.ICTDZZM3SKDMH5CK.SEARCH&ppt=sp&ppn=sp&ssid=xjzf96jejraelkao1765115855703&qH=0bdf574e7271bfc4"

response = requests.get(url=url, headers=headers)

tracking_data = response.text

soup = BeautifulSoup(tracking_data, "html.parser")

price_tag = list(soup.find(name="div", class_="hZ3P6w bnqy13").getText())

price = ""
for i in price_tag:
    if (i == "₹" or i == ","):
        continue
    else:
        price += i

price = int(price)

if price < TARGET_PRICE:
    send_mail()
