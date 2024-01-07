#!/usr/bin/python3
""" Python script that fetches"""
import requests
if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    r = response.encoding
    print("Body response:")
    print(f'\t- type: {type(r)}')
    print(f'\t- content: {response.text}')
