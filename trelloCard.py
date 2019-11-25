import requests
import json


def createCard(title):

    with open('keys.json') as json_file:
        data = json.load(json_file)
        apiKey = data['key']
        #secret = data['secret']
        token = data['token']
        board = data['boardID']

    url = "https://api.trello.com/1/cards"

    # Need to get IdList 
    # IdList is part of a board, so I need to get board ID then List ID then create a card on the listId

    # can get ID list by following instructions here: https://www.reddit.com/r/trello/comments/4axfcd/where_is_my_trello_board_id/ and parsing json

    
    querystring = {"idList":board, "name": title, "pos":"top", "keepFromSource":"all","key":apiKey,"token": token}


    response = requests.request("POST", url, params=querystring)

    respJson = response.json()

    directLink= respJson['shortUrl']

    print(directLink)

