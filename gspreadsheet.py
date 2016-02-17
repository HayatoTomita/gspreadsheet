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
        wsheet = getWorkSheet(sheet_name)
        try:
            wsheet.update_cell(row, col, val)
            self.status = "update complete"
        except gspread.UpdateCellError:
            self.status = "update failed"
        self.printStatus()

    def getWorkSheet(self, sheet_name):
        try:
            wsheet = self.gfile.worksheet(sheet_name)
            self.status = "get worksheet"
        except gsprea.WorksheetNotFound:
            self.status = "workseet not found"
        self.printStatus()

    def printStatus(self):
        print(self.status)
