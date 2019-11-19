from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import requests


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

    # service object API
    service = build('drive', 'v3', credentials=creds)

    folderName = input('Add Folder Name: ')
    parentID = '18xjjE1XqCqNYU3OOWA4IhivndT16uFBh'
    templateID = '1ALPBQ_8KG5LYH8RkvDwKjW9bwMx0j-uIaVpKS2cHwIM'

    body = {
          'name': folderName,
          'mimeType': "application/vnd.google-apps.folder"
        }
    if parentID:
        body['parents'] = [parentID]
    new_folder = service.files().create(body = body).execute()
    
    case_google_id = new_folder['id']
    folderTemplateList = ['screenshots', 'tests']

    for folderType in folderTemplateList:
        subBody = {
            'name': folderType,
            'mimeType': "application/vnd.google-apps.folder",
            'parents': [case_google_id]
        }
        subfolder = service.files().create(body = subBody).execute()
        print(subfolder['id'])

    copyFile = service.files().copy(fileId= templateID, body={'parents': [case_google_id], 'name': folderName}).execute()



if __name__ == '__main__':
    main()