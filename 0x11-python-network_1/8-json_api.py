#!/usr/bin/python3
"""script that takes in a letter and sends a POST request"""
import requests
import sys
if __name__ == "__main__":
    q = ""
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        q = {'q': sys.argv[1]}
    response = requests.post(url, data=q)
    try:
        r = response.json()
        if r == {}:
            print('No result')
        else:
            print(f"[{r.get('id')}] {r.get('name')}")
    except ValueError:
        print('Not a valid JSON')
