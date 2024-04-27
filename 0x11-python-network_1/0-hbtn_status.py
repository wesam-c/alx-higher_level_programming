#!/usr/bin/python3
""" Script fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import urllib.request
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        encoding = response.headers.get_content_charset()
        body = response.read()
        print('Body response:')
        print(f'\t- type: {type(body)}')
        print(f'\t- content: {body}')
        print(f'\t- utf8 content: {body.decode(encoding)}')
