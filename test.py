import requests
import os

GENDERIZED_KEY = os.getenv("GENDERIZED_KEY")
NAME = "Alexis"

response = requests.get(url=f"https://api.agify.io/?name={NAME}")
age_data = response.json()
print(age_data["age"])

response = requests.get(url=f"https://gender-api.com/get?name={NAME}&country=CA&key={GENDERIZED_KEY}")
gender_data = response.json()
print(gender_data["gender"])
