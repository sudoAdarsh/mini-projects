from dotenv import load_dotenv
import os
import requests

load_dotenv(os.path.expanduser("/home/adarshu/Documents/Coding/Python/mini-projects/.env"))

# response = requests.get(url=SHEETY_ENDPOINT, headers=bearer_header)
# pprint(response.json())
class DataManager:

    def __init__(self):
        self.SHEETY_API = os.getenv("SHEETY_API")
        self.AUTH_KEY = os.getenv("AUTH_KEY")

        self.bearer_header = {
            "Authorization": self.AUTH_KEY
        }

        self.SHEETY_ENDPOINT = f"https://api.sheety.co/{self.SHEETY_API}/flightDeals/prices"
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=self.SHEETY_ENDPOINT, headers=self.bearer_header)
        data = response.json()['prices']
        self.destination_data = data
        return self.destination_data
    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.SHEETY_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.bearer_header
            )
            print(response.text)