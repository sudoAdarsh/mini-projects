from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager
import time

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "BOM"

# Updating sheets if it does not ahve IATA code for city

# for row in sheet_data:
#     if row["iataCode"] == "":
#         row["iataCode"] = flight_search.get_destination_code(row["city"])
#         # slowing down requests to avoid rate limit
#         time.sleep(2)
# print(f"sheet_data:\n {sheet_data}")

# data_manager.destination_data = sheet_data
# data_manager.update_destination_codes()

d_day = int(input("Departure \ndate: "))
d_month = int(input("month: "))
d_year = int(input("year: "))
print()
r_day = int(input("Return \ndate: "))
r_month = int(input("month: "))
r_year = int(input("year: "))

departure = datetime(day=d_day, month=d_month, year=d_year)
return_date = datetime(day=r_day, month=r_month, year=r_year)

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"],
        from_time=departure,
        to_time=return_date
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: ₹{cheapest_flight.price}")
    time.sleep(2)
    if cheapest_flight.price != "N/A":
        notification_manager.send_mail(
            message=f"Subject:Time to travel 🛫 \n\nLow price alert! Only ₹{cheapest_flight.price} to fly from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, on {cheapest_flight.out_date} until {cheapest_flight.return_date}.".encode("utf-8")
            )