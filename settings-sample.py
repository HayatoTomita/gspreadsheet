import json
from oauth2client.client import SignedJwtAssertionCredentials

DOC_ID = 'SPREAD_SHEET_ID(URL)'

JSON_KEY = json.load(open('KEY_FILE_PATH(jsonFile)'))

SCOPE = ['https://spreadsheets.google.com/feeds']

CREDENTIALS = SignedJwtAssertionCredentials(
                 JSON_KEY['client_email'],
                 JSON_KEY['private_key'].encode(),
                 SCOPE)
