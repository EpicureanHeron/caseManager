## Purpose

Part of my business process involves creating documentation and saving it to Google Drive and then tracking cases via Trello for updates. Currently have to manually create folders, subfolders, new templates, and a Trello Card. This script automates all of that. 

## What it does

Creates a Google Drive Folder with the following contents

* Screenshots Subfolder
* Tests Subfolder
* Copy of Google Doc Template file

Creates a Trello card on CR Cases FY20 

* Same name as Google Drive Folder

## API Documentation

* [Google Drive](https://developers.google.com/drive/api/v3/about-sdk)
* [Google Docs](https://developers.google.com/docs/api)
* [Trello](https://developers.trello.com/reference/)

## To Dos

* Create doc in Google Drive Folder with Trello short links to card and email address for trello card
    * Doc is created and written to, but the email is not available yet
* [Link Google Drive Folder to Trello Card](https://trello.com/power-ups/55a5d916446f517774210006/google-drive)
* ~~At the very least, link in comment on Trello card back to the Google Drive folder (could be in summary at top)~~
* Add an example keys.json file
* According to documentation found on stackoverflow (?) unable to GET card email from API. Might need to load page by requesting .json and then loading the email from that query. 
