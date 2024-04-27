#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
import urllib.request
import sys
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data_encoded = urllib.parse.urlencode({'email': email})
    data_encoded = data_encoded.encode('ascii')
    request = urllib.request.Request(url, data_encoded)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode())
