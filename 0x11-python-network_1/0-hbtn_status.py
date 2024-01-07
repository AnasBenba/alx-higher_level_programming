#!/usr/bin/python3
"""Python script that fetches 
https://alx-intranet.hbtn.io/status"""
import urllib.request
if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        content = response.read()
        decoded_content = content.decode('utf-8')
        print("Body response:")
        print(f"    - type: {type(content)}")
        print(f"    - content: b'{decoded_content}'")
        print(f"    - utf-8 content: {decoded_content}")

