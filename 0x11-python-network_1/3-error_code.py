#!/usr/bin/python3
"""
importing files from request
"""

import urllib.request
import urllib.error
import sys

def send_request_and_display_body(url):
    try:
        # Send a request to the specified URL
        with urllib.request.urlopen(url) as response:
            # Read and decode the response body
            response_body = response.read().decode('utf-8')
            print(response_body)

    except urllib.error.HTTPError as e:
        # If an HTTP error occurs, print the error code
        print(f"Error code: {e.code}")

if __name__ == "__main__":
    # Get URL from command line arguments
    url = sys.argv[1]

    # Call the function to send the request and display the body
    send_request_and_display_body(url)
