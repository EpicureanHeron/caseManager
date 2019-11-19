import requests
import json


def createCard(title):

    with open('keys.json') as json_file:
        data = json.load(json_file)
        apiKey = data['key']
        token = data['secret']

    url = "https://api.trello.com/1/cards"


    querystring = {"idList":"idList","keepFromSource":"all","key":apiKey,"token": token}

    print(querystring)

    response = requests.request("POST", url, params=querystring)

    print(response.text)

createCard('check')