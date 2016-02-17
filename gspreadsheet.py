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
        wsheet = self.getWorkSheet(sheet_name)
        try:
            wsheet.update_cell(row, col, val)
            self.status = "update complete"
        except gspread.UpdateCellError:
            self.status = "update failed"
        self.printStatus()

    def find(self, sheet_name, query):
        wsheet = self.getWorkSheet(sheet_name)
        try:
            cell = wsheet.find(query)
            self.status = "find in " + str(cell.row) + "," + str(cell.col)
            self.printStatus()
            return cell.row, cell.col
        except gspread.CellNotFound:
            self.status = "no cells found value:" + str(query)
            self.printStatus()
            return None, None

    def getWorkSheet(self, sheet_name):
        try:
            wsheet = self.gfile.worksheet(sheet_name)
            self.status = "get worksheet"
            self.printStatus()
            return wsheet
        except gspread.WorksheetNotFound:
            self.status = "workseet not found"
            self.printStatus()
            return None

    def printStatus(self):
        print(self.status)
