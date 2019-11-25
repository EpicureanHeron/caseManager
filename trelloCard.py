import requests
import json


def createCard(title, google_id):

    with open('keys.json') as json_file:
        data = json.load(json_file)
        apiKey = data['key']
        token = data['token']
        board = data['boardID']

    url = "https://api.trello.com/1/cards"

    # can get ID list by following instructions here: https://www.reddit.com/r/trello/comments/4axfcd/where_is_my_trello_board_id/ and parsing json

    folderURL = 'https://drive.google.com/drive/folders/%s' % google_id

    folderMarkdown = '[Link to Google Drive Folder](%s)' % folderURL

    querystring = {"idList":board, "name": title, "desc": folderMarkdown, "pos":"top", "keepFromSource":"all","key":apiKey,"token": token}

    response = requests.request("POST", url, params=querystring)

    respJson = response.json()
    print(respJson)

    directLink= respJson['shortUrl']
    print('------trelloCard 28')
    print(directLink)
    #print(google_id)
    
    print(folderURL)
    email = respJson['email']
    print(email)

    return(email, directLink)

