#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
import requests
import sys

if __name__ == "__main__":
    value = ""
    if len(sys.argv) > 1:
        value = sys.argv[1]
    data = {"q": value}
    response = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        json_response = response.json()
        if json_response:
            print(f'[{json_response.get("id")}] {json_response.get("name")}')
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
