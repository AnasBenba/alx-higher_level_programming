#!/usr/bin/python3
"""script that takes your GitHub credentials
to display your id"""
import requests
import sys


if __name__ == "__main__":
    url = f'https://api.github.com/repos/{sys.argv[1]}/{sys.argv[2]}/commits'
    responde = requests.get(url)
    r = responde.json()
    for i in range(0, 10):
        print(f"{r[i]['sha']}: {r[i]['commit']['author']['name']}")
