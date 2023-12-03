#!/usr/bin/python3
"""
This module fetches the status of the URL https://alx-intranet.hbtn.io/status
and displays the body of the response in a tabulated format.
"""


from urllib import request, error


def fetch_status(url):
    """
    Fetches the status of the given URL and displays the body of the response.
    """
    try:
        with request.urlopen(url) as response:
            content = response.read().decode('utf-8')

        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
    except error.URLError as e:
        print(f"Error fetching the URL: {e}")

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    fetch_status(url)
