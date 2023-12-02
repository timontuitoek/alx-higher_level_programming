#!/usr/bin/python3


"""
This module takes a URL and an email as command-line arguments, sends a POST
request to the specified URL with the email as a parameter, and displays the
body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.parse
import sys

def send_post_request(url, email):
    """
    Sends a POST request to the specified URL with the email as a parameter.

    Args:
    - url (str): The URL to send the POST request to.
    - email (str): The email to be sent as a parameter.
    """
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    
    with urllib.request.urlopen(url, data=data) as response:
        content = response.read().decode('utf-8')
    
    print(content)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <http://0.0.0.0:5000> <hr@holbertonschool.com>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
