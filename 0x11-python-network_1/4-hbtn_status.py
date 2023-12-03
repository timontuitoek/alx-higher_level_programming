#!/usr/bin/python3
"""
This script takes a URL as input, sends a request to the URL, and displays the value of the variable X-Request-Id in the response header.
"""

import sys
import urllib.request
import urllib.error

def get_url_content(url):
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python get_url_content.py <URL>")
    else:
        get_url_content(sys.argv[1])
