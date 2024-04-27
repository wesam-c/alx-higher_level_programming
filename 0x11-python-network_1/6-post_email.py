#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
import requests
import sys

if __name__ == "__main__":
    data = {"email": sys.argv[2]}
    req = requests.post(sys.argv[1], data=data)
    print(req.text)
