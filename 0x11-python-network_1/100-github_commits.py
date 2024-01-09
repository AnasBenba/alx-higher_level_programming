#!/usr/bin/python3
"""script that takes your GitHub credentials
to display your id"""
import requests
import sys

if __name__ == '__main__':
    url = f'https://api.github.com/repos/{sys.argv[1]}/{sys.argv[2]}/commits'
    responde = requests.get(url)
    r = responde.json()
    j = 0
    for i in range(len(r)):
        for j in range(0, j-i-1):
            date1 = int(r[j]['date'].split('T')[0].split('/', ''))
            date2 = int(r[j+1]['date'].split('T')[0].split('/', ''))
            if date1 < date2:
                r[j], r[j+1] = r[j+1], r[j]
    for i in range(0, 10):
        print(f"{r[i]['sha']}: {r[i]['commit']['author']['name']}")
