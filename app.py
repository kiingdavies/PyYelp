# Pip install requests package
# import requests
# import config file where api_key is stored
# git ignore the config.py file
# get yelp business search url
# get yelp business search api_key
# headers dictionary with Authentication
# params dictionary  with location to "NYC" or "LA" etc
# requests.get takes in url, headers & params
# print(response.text)

import requests
import config

url = "https://api.yelp.com/v3/businesses/search"

headers = {
    "Authorization": "Bearer " + config.api_key
}

params = {
    "term": "Barber",
    "location": "LA"
}


response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]
names = [business["name"] for business in businesses if business["rating"] > 4.5]
print(names)
