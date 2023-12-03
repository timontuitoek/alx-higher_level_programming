#!/usr/bin/python3
"""
Fetches the URL: https://alx-intranet.hbtn.io/status
"""

from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    req = Request(url)

    with urlopen(req) as response:
        raw_content = response.read()
        decoded_content = raw_content.decode('utf-8')

        print('Body response:')
        print('\t- type: {_type}'.format(_type=type(raw_content)))
        print('\t- content: {_content}'.format(_content=raw_content))
        print('\t- utf8 content: {_utf8_c}'.format(_utf8_c=decoded_content))
