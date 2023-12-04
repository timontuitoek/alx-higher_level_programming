#!/usr/bin/python3
"""
This script takes a URL as input, sends a request to the URL, and displays the value of the variable X-Request-Id in the response header.
"""

import requests
import subprocess
import shlex

def run_command(command):
    try:
        process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
        output, error = process.communicate()
        return output, error
    except Exception as e:
        return None, str(e)

def fetch_status():
    url = "https://alx-intranet.hbtn.io/status"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        print("\n".join([f"{key}: {value}" for key, value in data.items()]))

    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Something went wrong:", err)

def main():
    fetch_status()

if __name__ == "__main__":
    main()
