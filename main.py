## --------------- This makes a visual habit tracker ---------- #
## -------- It uses the API at pixe.la ----------------------- ##
import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "tomskeeeeee"
TOKEN = "G#*+!e4MJsE2I3YgB"
# ----------- Step 1 Create a user -------------- #
# example POST request parameters:
# {"token":"thisissecret", "username":"a-know", "agreeTermsOfService":"yes", "notMinor":"yes"}

user_params = {
    # token - you make this up, 8 - 128 characters
    # uncomment out the lines below this to create the user
    "token": "G#*+!e4MJsE2I3YgB",
    "username": "replace with your desired name",
    "agreeTermsOfService": "yes",
    "notMinor":"yes",
}

# uncomment to create user, comment out and replace username variable once successful
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# ---------- Step 2 make new graph -------------- #
# required Keys:
# id (unique), Validation rule: ^[a-z][a-z0-9-]{1,16}
# Must start with letter, then letter/number combos, 1 - 16 chars
# name,
# unit (ex: pound, commit, minutes)
# type - int or float
# color - for pixels - options are (these are strings):
# shibafu (green), momiji (red), sora (blue), ichou (yellow), ajisai (purple) and kuro (black)
# options key: timezone (ex: CT ??)

graph_config = {
    "id": "coding",
    "name": "Coding Habit Tracker",
    "unit": "hour",
    "type": "int",
    "color": "ajisai",
    "timezone": "America/Chicago",
}
# Pass in authentication via an HTTP header, not in the actual request
headers = {
    "X-USER-TOKEN": TOKEN
}

# Graph is at: https://pixe.la/v1/users/<username>/graphs/<graphID>
# Code below makes the graph "Coding Habit Tracker" from above
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# ------------ Step 3 - Adding a pixel to the graph ----------- #

data = input("How many hours did you code today? ")
# endpoint template: https://pixe.la/v1/users/<username>/graphs/<graphID>
add_pixel_endpoint = "https://pixe.la/v1/users/tomskeeeeee/graphs/coding"

# required keys:
# date - The date on which the quantity is to be recorded. It is specified in yyyyMMdd format.
# quantity - string
# ------------ Automatically add date in proper format ------- #
# today = datetime(year=2021, month=8, day=9)  -- if you want to add older days
today = datetime(year=2021, month=8, day=6)
proper_date = today.strftime("%Y%m%d")   # 20210810
# print(today.strftime("%Y-%m-%d"))     # 2021-08-10

pixel_params = {
    "date": proper_date,
    "quantity": data,
}

response = requests.post(url=add_pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)

# ------------ Step 4 - PUT Requests to update exisiting data ------ #
put_endpoint = f"https://pixe.la/v1/users/tomskeeeeee/graphs/coding/{proper_date}"
# required key: quantity
put_params = {
    "quantity": "350"
}

# response = requests.put(url=put_endpoint, json=put_params, headers=headers)
# print(response.text)

# ----------- Step 5 - Delete exisitng data ------- #
delete_endpoint = f"https://pixe.la/v1/users/tomskeeeeee/graphs/coding/20200810"
# no data needed
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)