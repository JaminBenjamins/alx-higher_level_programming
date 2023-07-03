#!/usr/bin/python3
"""
    Takes an URL and sends request and display
    back the body of response handling exceptions
"""

import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
