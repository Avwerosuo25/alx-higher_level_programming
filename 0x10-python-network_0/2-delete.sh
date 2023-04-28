#!/bin/bash
#this send a DELETE request using curl
curl -s -o /dev/null -w "%{http_code}" -X DELETE "$url"
