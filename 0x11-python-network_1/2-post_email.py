#!/usr/bin/python3
"""
This module takes a URL and an email as command-line arguments, sends a POST
request to the specified URL with the email as a parameter, and displays the
body of the response (decoded in utf-8).
"""

import urllib.parse
import urllib.request
import sys

def send_post_request(url, email):
    # Encode the email as a parameter
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Send a POST request to the specified URL
    with urllib.request.urlopen(url, data=data) as response:
        # Read and decode the response body
        response_body = response.read().decode('utf-8')
        print(response_body)

if __name__ == "__main__":
    # Get URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Call the function to send the POST request
    send_post_request(url, email)
