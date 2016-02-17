# -*- coding:utf-8 -*-
import gspread
from oauth2client.client import SignedJwtAssertionCredentials


class GSpreadSheet:
    def __init__(self):
        self.status = "initialized"
        self.printStatus()

    def connect(self, credentials, doc_id):
        try:
            self.gc = gspread.authorize(credentials)
            self.gfile = self.gc.open_by_key(doc_id)
            self.status = "connected"
        except gspread.AuthenticationError:
            self.status = "connection failed"
        self.printStatus()

    def update(self, sheet_name, row, col, val):
        try:
            wsheet = self.gfile.worksheet(sheet_name)
            self.status = "update complete"
        except gspread.WorksheetNotFound:
            self.status = "worksheet not found"
        wsheet.update_cell(row, col, val)
        self.printStatus()

    def printStatus(self):
        print(self.status)
