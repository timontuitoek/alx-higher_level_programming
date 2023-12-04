#!/usr/bin/python3
"""
Importing files
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    x_request_id = response.headers.get('X-Request-Id')

    if x_request_id is not None:
        print(x_request_id)
    else:
        print("X-Request-Id not found in the response headers.")
