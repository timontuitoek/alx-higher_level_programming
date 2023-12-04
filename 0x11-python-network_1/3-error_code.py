#!/usr/bin/python3
"""
importing files from request
"""

import sys
import urllib.request


def get_url_content(url):
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            print(html)

    except urllib.error.HTTPError as errh:
        print(f'Error code: {errh.code}')
    except urllib.error.URLError as erru:
        print(f'URL Error: {erru.reason}')
    except Exception as err:
        print(f'Error: {err}')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please provide a URL as argument.')
    else:
        get_url_content(sys.argv[1])
