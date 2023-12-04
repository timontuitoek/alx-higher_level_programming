#!/usr/bin/python3
"""_
Importing files
"""

import requests
import sys

def fetch_x_request_id(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(f"X-Request-Id: {x_request_id}")
        else:
            print("X-Request-Id header not found in the response.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Example usage
url_to_fetch = sys.argv[1]
fetch_x_request_id(url_to_fetch)
