#!/usr/bin/python3
""" A script that fetches a url
using urllib package
"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        response = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(responses)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode(encoding='utf-8')))
