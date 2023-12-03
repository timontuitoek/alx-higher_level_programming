#!/usr/bin/python3
"""
This module takes a URL as a command-line argument, sends a request to the URL,
and displays the value of the X-Request-Id variable found in the header of the response.
"""


import urllib.request
import sys


def fetch_x_request_id(url):
    """
    Fetches the value of the X-Request-Id variable from the header of the response
    """
    try:
        req = urllib.request.Request(url)
        
        with urllib.request.urlopen(req) as response:
            x_request_id = response.headers.get('X-Request-Id')
        
        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id not found in the response header.")
    except urllib.error.URLError as e:
        print(f"Error fetching the URL: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    fetch_x_request_id(url)
