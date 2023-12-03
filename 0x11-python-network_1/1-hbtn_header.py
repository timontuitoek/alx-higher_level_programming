#!/usr/bin/python3
"""
This module takes a URL as a command-line argument, sends a request to the URL,
and displays the value of the X-Request-Id variable found in the header of the response.
"""


import urllib.request
import sys


def get_x_request_id(url):
    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.getheader('X-Request-Id')
            if x_request_id:
                print(f"The value of X-Request-Id is: {x_request_id}")
            else:
                print("X-Request-Id header not found in the response.")
    except urllib.error.URLError as e:
        print(f"Error connecting to the URL: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a URL as a command-line argument.")
    else:
        url = sys.argv[1]
        get_x_request_id(url)
