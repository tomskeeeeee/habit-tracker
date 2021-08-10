## --------------- This makes a visual habit tracker ---------- #
## -------- It uses the API at pixe.la ----------------------- ##
import requests

pixela_endpoint = "https://pixe.la/v1/users"
# Create a user
# example POST request parameters:
# {"token":"thisissecret", "username":"a-know", "agreeTermsOfService":"yes", "notMinor":"yes"}

user_params = {
    # token - you make this up, 8 - 128 characters
    "token": "G#*+!e4MJsE2I3YgB",
    "username": "tomskeeeeee",
    "agreeTermsOfService": "yes",
    "notMinor":"yes",
}
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)