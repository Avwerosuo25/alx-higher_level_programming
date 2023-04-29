#!/usr/bin/python3
"""
A script that sends a POST request to a given URL with an email parameter
and displays the body of the response.

Usage: ./post_email.py <URL> <email>
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    # Retrieve URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode email as UTF-8 and build request object
    email_bytes = email.encode("utf-8")
    headers = {"Content-Type": "application/x-www-form-urlencoded", "Content-Length": len(email_bytes)}
    request = urllib.request.Request(url, data=email_bytes, headers=headers)

    # Send POST request and print response body
    with urllib.request.urlopen(request) as response:
        body = response.read().decode("utf-8")
        print(body)
