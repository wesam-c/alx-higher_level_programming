#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    headers = {"Accept": "application/vnd.github.v3+json",
                "X-GitHub-Api-Version": "2022-11-28",
                "Authorization": f"Bearer {password}"}
    response = requests.get(url, headers=headers)
    
    print(response.json().get("id"))
