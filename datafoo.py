import requests
import json

ENDPOINT = 'http://www.saferproducts.gov/RestWebServices/Recall'


def get_data():
    resp = requests.get(ENDPOINT, params={'format': 'json', 'RecallDateStart': 2016})
    return json.loads(resp.text)
