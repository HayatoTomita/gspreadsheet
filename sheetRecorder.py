# -*- coding:utf-8 -*-
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
import settings

CREDENTIALS = SignedJwtAssertionCredentials(
                 settings.JSON_KEY['client_email'],
                 settings.JSON_KEY['private_key'].encode(),
                 settings.SCOPE)


def main():
    gc = gspread.authorize(CREDENTIALS)
    gfile = gc.open_by_key(settings.DOC_ID)
    wsheet = gfile.get_worksheet(1)
    wsheet.update_acell('C3', 'hoge')
    records = wsheet.get_all_records()

    for record in records:
        print(record)

if __name__ == '__main__':
    main()
