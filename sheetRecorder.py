# -*- coding:utf-8 -*-
"""sheetRecorder

Record some values to GoogleSpreadSheet
Usage:
  sheetRecorder.py <sheet_name> <row> <col> <value> [options]

Options:
  -h --help                Show this screen.
  --version                Show version.
"""
from docopt import docopt
import settings
import gspreadsheet


if __name__ == '__main__':
    args = docopt(__doc__, version="0.0.1")
    sheet = gspreadsheet.GSpreadSheet()
    sheet.connect(settings.CREDENTIALS, settings.DOC_ID)
    sheet.update(
        args['<sheet_name>'],
        args['<row>'],
        args['<col>'],
        args['<value>'])
    print("finish")
