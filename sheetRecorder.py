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
from oauth2client.client import SignedJwtAssertionCredentials
import settings
import gspreadsheet

CREDENTIALS = SignedJwtAssertionCredentials(
                 settings.JSON_KEY['client_email'],
                 settings.JSON_KEY['private_key'].encode(),
                 settings.SCOPE)


if __name__ == '__main__':
    args = docopt(__doc__, version="0.0.1")
    sheet = gspreadsheet.GSpreadSheet()
    sheet.connect(CREDENTIALS, settings.DOC_ID)
    sheet.update(
        args['<sheet_name>'],
        args['<row>'],
        args['<col>'],
        args['<value>'])
    print("finish")
