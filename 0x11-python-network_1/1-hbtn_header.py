#!/usr/bin/python3
"""Takes a URL sends a request to the URL and fetches
the X-Request-Id parameter found in header of response
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers.)get("X-Request-Id"))
