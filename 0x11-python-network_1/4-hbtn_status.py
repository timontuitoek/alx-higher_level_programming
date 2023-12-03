#!/usr/bin/python3
"""
This script takes a URL as input, sends a request to the URL, and displays the value of the variable X-Request-Id in the response header.
"""

import urllib.request
from urllib.error import HTTPError
import sys

def fetch_url(url):
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print(f"Error code: {e.code}")

# Example usage
url_to_fetch = sys.argv[1]
fetch_url(url_to_fetch)
