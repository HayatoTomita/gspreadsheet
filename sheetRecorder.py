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


def update(args):
    gc = gspread.authorize(CREDENTIALS)
    gfile = gc.open_by_key(settings.DOC_ID)
    wsheet = gfile.worksheet(args['<sheet_name>'])
    wsheet.update_acell(args['<cell_number>'], args['<value>'])

if __name__ == '__main__':
    args = docopt(__doc__, version="0.0.1")
    update(args)
