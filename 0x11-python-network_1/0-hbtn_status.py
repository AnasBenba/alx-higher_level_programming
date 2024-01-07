#!/usr/bin/python3
"""Python script that fetches"""
import urllib.request
if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        content = response.read()
        decoded_content = content.decode('utf-8')
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: b'{decoded_content}'")
        print(f"\t- utf8 content: {decoded_content}")
