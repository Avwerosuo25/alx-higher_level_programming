#!/usr/bin/python3
"""A script that takes 2 arguments: the repository name and owner name, and
sends a GET request to the GitHub API to obtain the id of the user
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/'.format(sys.argv[2], sys.argv[1])
    response = requests.get(url, auth=(sys.argv[3], sys.argv[4]))
    try:
        print(response.json().get('id'))
    except ValueError:
        print('Not a valid JSON')
