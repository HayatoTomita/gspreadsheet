# -*- coding:utf-8 -*-
"""sheetRecorder

Record some values to GoogleSpreadSheet
Usage:
  sheetRecorder.py <sheet_name> <cell_number> <value> [options]

Options:
  -h --help                Show this screen.
  --version                Show version.
"""
from docopt import docopt


import gspread
from oauth2client.client import SignedJwtAssertionCredentials
import settings

CREDENTIALS = SignedJwtAssertionCredentials(
                 settings.JSON_KEY['client_email'],
                 settings.JSON_KEY['private_key'].encode(),
                 settings.SCOPE)


class GSpreadSheet:
    def __init__(self):
        self.status = "initialized"
        self.printStatus()

    def connect(self, credentials):
        try:
            self.gc = gspread.authorize(credentials)
            self.gfile = self.gc.open_by_key(settings.DOC_ID)
            self.status = "connected"
        except gspread.AuthenticationError:
            self.status = "connection failed"
        self.printStatus()

    def update(self, args):
        try:
            wsheet = self.gfile.worksheet(args['<sheet_name>'])
            self.status = "update complete"
        except gspread.WorksheetNotFound:
            self.status = "worksheet not found"
        wsheet.update_acell(args['<cell_number>'], args['<value>'])
        self.printStatus()

    def printStatus(self):
        print(self.status)

if __name__ == '__main__':
    args = docopt(__doc__, version="0.0.1")
    sheet = GSpreadSheet()
    sheet.connect(CREDENTIALS)
    sheet.update(args)
    print("finish")
