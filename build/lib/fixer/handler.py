import json
import requests

BASE_PATH = 'http://data.fixer.io/api/latest?access_key='


def get_rates(API_KEY):
    """ it will make a get request, take the response and return the JSON 

    :return: the information about the rates
    :rtype: json
    """
    response = requests.get(BASE_PATH + API_KEY)
    if response.status_code == 200:
        return json.loads(response.text)
    return None
