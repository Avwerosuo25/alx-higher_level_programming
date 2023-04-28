#!/bin/bash

# Display the body of the response for a 200 status code

response=$(curl -s -o /dev/null -w "%{http_code}" $1)
if [[ $response == 200 ]]; then
  curl -sL $1
else
  echo "Error: HTTP status code $response"
fi
