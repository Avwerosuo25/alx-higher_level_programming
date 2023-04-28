#!/bin/bash
#this send a DELETE request using curl
url=$1
response=$(curl -s -o /dev/null -w "%{http_code}" -X DELETE "$url")
