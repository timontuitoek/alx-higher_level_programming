#!/usr/bin/python3
"""
This script takes a URL as input, sends a request to the URL, and displays the value of the variable X-Request-Id in the response header.
"""

import requests
import sys

def get_x_request_id(url):
    """
    Sends a request to the specified URL and retrieves the value of the X-Request-Id variable from the response header.

    :param url: The URL to send the request to.
    """
    try:
        response = requests.get(url)
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(f"The value of X-Request-Id is: {x_request_id}")
        else:
            print("X-Request-Id not found in the response headers.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    get_x_request_id(url)
