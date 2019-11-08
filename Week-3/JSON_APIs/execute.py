term = 'Plumbers'
location = 'Bushwick NY'
url_params = {  'term': term.replace(' ', '+'),
                'location': location.replace(' ', '+'),
                'limit' : 50,
                'offset' : 0
             }


url = https://api.yelp.com/v3/businesses/{id}/reviews
headers = {'Authorization': 'Bearer {}'.format(api_key)}
response = requests.get(url, headers=headers, params=url_params)



import json
import requests
import time