import requests

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Scheme:", data["meta"]["scheme_name"])
    print("Latest NAV:", data["data"][0])
else:
    print("Failed to fetch data")