import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv(os.path.expanduser("/home/adarshu/Documents/Coding/Python/mini-projects/.env"))

TOKEN = os.getenv("PIXELA_TOKEN")
USER_NAME = "adarsh01"
GRAPH = "graph1"


pixela_endpoint = "https://pixe.la/v1/users"

user_paramas = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH,
    "name": "Coding Graph",
    "unit": "Hrs",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()
today = datetime(year=2025, month=11, day=27)
pixel_config = {
    "date": today.strftime("%Y%m%d") ,
    "quantity": "0",
}

pixel_endpoint = f"{graph_endpoint}/{GRAPH}"

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)