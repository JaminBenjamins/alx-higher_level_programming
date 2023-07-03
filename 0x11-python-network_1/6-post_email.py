#!/usr/bin/python3
"""
    Script that takes a URL and email and send POST request
    then rturn the body response
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    r = request.post(url, data={'email': email})
    print(r.text)
