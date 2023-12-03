#!/usr/bin/python3
"""
importing files from request
"""

import urllib.request
import urllib.error
import sys

def send_request_and_display_body(url):
    try:
        with urllib.request.urlopen(url) as response:
            response_body = response.read().decode('utf-8')
            print(response_body)

    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

if __name__ == "__main__":
    url = sys.argv[1]

    send_request_and_display_body(url)
