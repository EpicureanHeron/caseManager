import requests
import json


def createCard(title):

    with open('keys.json') as json_file:
        data = json.load(json_file)
        apiKey = data['key']
        #secret = data['secret']
        token = data['token']

    url = "https://api.trello.com/1/cards"

    # Need to get IdList 
    # IdList is part of a board, so I need to get board ID then List ID then create a card on the listId

    
    querystring = {"idList":"idList","keepFromSource":"all","key":apiKey,"token": token}

    print(querystring)

    response = requests.request("POST", url, params=querystring)

    print(response.text)

createCard('check')