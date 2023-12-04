#!/usr/bin/python3
"""
Import requests
"""

import requests
import sys

def send_post_request(url, email):
    try:
        payload = {'email': email}
        response = requests.post(url, data=payload)
        response.raise_for_status()

        print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Example usage
url_to_post = sys.argv[1]
email_to_send = sys.argv[2]
send_post_request(url_to_post, email_to_send)
