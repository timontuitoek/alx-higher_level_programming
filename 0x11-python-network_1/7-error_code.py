#!/usr/bin/python3
'''
Import requests
'''

import requests
import sys

def fetch_url_body(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        print(response.text)

    except requests.exceptions.HTTPError as e:
        print(f"Error code: {e.response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Example usage
url_to_fetch = sys.argv[1]
fetch_url_body(url_to_fetch)
