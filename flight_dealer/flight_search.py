import os
import requests
from dotenv import load_dotenv
from pprint import pprint

load_dotenv(dotenv_path="/home/adarshu/Documents/Coding/Python/mini-projects/.env")

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:
    def __init__(self):
        self.AMADEUS_API_KEY = os.getenv("AMADEUS_API_KEY")
        self.AMADEUS_API_SECRET = os.getenv("AMADEUS_API_SECRET")
        self.AUTH_TOKEN = self.get_new_token()
    
    def get_new_token(self):
        header = {
            "Content-Type": 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.AMADEUS_API_KEY,
            'client_secret': self.AMADEUS_API_SECRET
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        return response.json()['access_token']

    def get_destination_code(self, city_name):
        headers = {"Authorization": f"Bearer {self.AUTH_TOKEN}"}
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(IATA_ENDPOINT, params=query, headers=headers)
        print(f"Status code: {response.status_code}, IATA Code: {response.text}")
    
    def find_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"Authorization": f"Bearer {self.AUTH_TOKEN}"}
        parameters = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": "1",
            "currencyCode": "INR",
            "nonstop": "true",
            "max": "10",
        }
        response = requests.get(url=FLIGHT_ENDPOINT, params=parameters, headers=headers)
        print(response.text)
f = FlightSearch()
f.find_flights()