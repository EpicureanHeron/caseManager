from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import requests
import json

import trelloCard
import googleDoc


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']


def main():


    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    # opens the keys.json which has the ID for the parent folder and the ID for the template folder 
    with open('keys.json') as json_file:
        data = json.load(json_file)
        parentID = data['GoogleDriveFolder']
        templateID = data["GoogleDocTemplate"]

    # service object API
    service = build('drive', 'v3', credentials=creds)

    # create name for folder and trello card
    folderName = input('Add Folder Name: ')


    # stages data for API folder creation 
    body = {
          'name': folderName,
          'mimeType': "application/vnd.google-apps.folder"
        }
    if parentID:
        body['parents'] = [parentID]
    new_folder = service.files().create(body = body).execute()
    
    # grabs the new folder's ID for reference 
    case_google_id = new_folder['id']

    # list of template folders to include 
    folderTemplateList = ['screenshots', 'tests']

    # loops through template list and adds them to the newly created folder 
    for folderType in folderTemplateList:
        subBody = {
            'name': folderType,
            'mimeType': "application/vnd.google-apps.folder",
            'parents': [case_google_id]
        }
        service.files().create(body = subBody).execute()
       

    # copys case template google doc to the new folder
    service.files().copy(fileId= templateID, body={'parents': [case_google_id], 'name': folderName}).execute()


    newCard = trelloCard.createCard(folderName, case_google_id)

    # email address may not be available: https://stackoverflow.com/questions/42247377/trello-api-e-mail-address-of-my-card-returns-null

    ## sounds like if you do newCard.json and load, and parse the json, the email address MIGHT be available (rather than using API, have to use direct REQUEST to the wbe facing version)

    newDocId = googleDoc.googleDoc(newCard, folderName)

    # trelloFile = drive_service.files().update(fileId=newDocId,


    trelloFile = service.files().get(fileId=newDocId, fields='parents').execute()
    

    previous_parents = ",".join(trelloFile.get('parents'))
# Move the file to the new folder
    trelloFile = service.files().update(fileId=newDocId,
                                    addParents=case_google_id,
                                    removeParents=previous_parents,
                                    fields='id, parents').execute()






    

if __name__ == '__main__':
    main()