#!/bin/bash
#Check if a URL is provided as an argument
if [ -z "$1" ]; then
    echo "Please provide a URL as an argument"
    exit 1
fi
response=$(curl -s "$1")
body_size=$(echo "$response" | wc -c)
echo "Response body size: $body_size bytes"
