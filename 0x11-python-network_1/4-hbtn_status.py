#!/usr/bin/python3
"""
import requests
"""

import requests

def get_status():
    try:
        response = requests.get('https://alx-intranet.hbtn.io/status')
        response.raise_for_status()

        data = response.json()
        print('- Status')
        for key, value in data.items():
            print(f'\t- {key}: {value}')

    except requests.exceptions.HTTPError as errh:
        print(f'HTTP Error: {errh}')
    except requests.exceptions.ConnectionError as errc:
        print(f'Error Connecting: {errc}')
    except requests.exceptions.Timeout as errt:
        print(f'Timeout Error: {errt}')
    except requests.exceptions.RequestException as err:
        print(f'Error: {err}')

if __name__ == '__main__':
    get_status()