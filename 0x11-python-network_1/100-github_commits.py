#!/usr/bin/python3
"""script that takes your GitHub credentials
to display your id"""
import requests
import sys


if __name__ == "__main__":
    resp = requests.get('https://api.github.com/repos/{}/{}/commits'
                        .format(sys.argv[2], sys.argv[1]))
    for commit in resp.json()[0:10]:
        print("{}: {}".format(commit.get('sha'),
                              commit.get('commit').get('author').get('name')))
