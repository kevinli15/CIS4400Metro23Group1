import requests

response = requests.get("https://data.ny.gov/resource/v7qc-gwpn.json")
metro = response.json()
print(metro[0]['station'])