#!/usr/bin/python3
"""
script that demonstrates how to use Basic Authentication
with the GitHub API and requests package to display your user id
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_id = response.json()["id"]
        print("Your user id is:", user_id)
    else:
        print("Error: failed to get user information")
