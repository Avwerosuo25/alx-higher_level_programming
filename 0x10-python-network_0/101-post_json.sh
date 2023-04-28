#!/bin/bash
# A script that sends JSON post request to a URL passed as the first argument
curl -s -X POST -d @"$2" -H "Content-Type: application/json" "$1"
