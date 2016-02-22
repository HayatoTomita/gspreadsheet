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

    def update(self, wsheet, row, col, val):
        try:
            wsheet.update_cell(row, col, val)
            self.status = "update complete"
        except gspread.UpdateCellError:
            self.status = "update failed"
        self.printStatus()

    def find(self, wsheet, query):
        try:
            cell = wsheet.find(query)
            self.status = "find in " + str(cell.row) + "," + str(cell.col)
            self.printStatus()
            return cell.row, cell.col
        except gspread.CellNotFound:
            self.status = "no cells found value:" + str(query)
            self.printStatus()
            return None, None

    def getRowList(self, wsheet, num):
        rowList = wsheet.row_values(num)
        return rowList

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

    def createFromTemplate(self, sheet_name, template_name):
        try:
            self.status = "start to copy template sheet"
            self.printStatus()
            wsheet = self.gfile.add_worksheet(sheet_name,30,40)
            template = self.getWorkSheet(template_name)
            list = template.get_all_values()
            row_len = len(list)
            col_len = len(list[0])
            end_cell = template.get_addr_int(row_len,col_len)
            range_str = "A1:" + str(end_cell)
            cell_list = template.range(range_str)
            for i in cell_list:
                if i.value == "":
                     continue
                wsheet.update_cell(i.row,i.col,i.value)

        except gspread.WorksheetNotFound:
            self.status = "template sheet not found"
            self.printStatus()


    def printStatus(self):
        print(self.status)
