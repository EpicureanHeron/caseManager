from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.


# The ID of a sample document.


def googleDoc(link, folderName):
    SCOPES = ['https://www.googleapis.com/auth/documents']
    #print(email)
    print(link)
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token2.pickle'):
        with open('token2.pickle', 'rb') as token:
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
        with open('token2.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('docs', 'v1', credentials=creds)

    
    body = {
        'title': 'Trello Info %s' % folderName
    }


    doc = service.documents().create(body=body).execute()

  
    text = """
    email: 'See Card Link'  
    card link: %s
    """ % (link)

    requests = [
         {
            'insertText': {
                'location': {
                    'index': 1,
                },
                'text': text
            }
        }

    ]

    service.documents().batchUpdate(documentId=doc['documentId'], body={'requests': requests}).execute()

    return(doc['documentId'])

