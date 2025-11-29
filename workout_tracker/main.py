import os 
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv(os.path.expanduser("/home/adarshu/Documents/Coding/Python/mini-projects/.env"))

app_id = os.getenv("NUTRITION_API_ID")
app_key = os.getenv("NUTRITION_API_KEY")
api_key = os.getenv("SHEETY_API")
auth_key = os.getenv("AUTH_KEY")

endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

headers = {
    "x-app-id": app_id,
    "x-app-key": app_key
}

bearer_header = {
    "Authorization": auth_key
}

all_task = input("What exercise you did today: ")
tasks = all_task.split(" and ")

for task in tasks:
    query_body = {
        "query": task,
        "weight_kg": 74,                  
        "height_cm": 173,              
        "age": 18,                        
        "gender": "male"
    }

    response = requests.post(url=endpoint, json=query_body, headers=headers)
    data = response.json()
    exercise = data["exercises"][0]['name'].title()
    duration = data["exercises"][0]['duration_min']
    calories = data["exercises"][0]['nf_calories']
    time = datetime.now().strftime("%X")
    date = datetime.now().strftime("%d/%m/%Y") 


    sheety_endpoint = f"https://api.sheety.co/{api_key}/workoutTracking/workouts"
    sheets_data = {
        'workout':{
            'date': date,
            'time': time,
            'exercise': exercise,
            'duration': duration,
            'calories': calories,
        }
    }
    response = requests.post(url=sheety_endpoint, json=sheets_data, headers=bearer_header)
    print(response.text)

