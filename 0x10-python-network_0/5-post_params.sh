#!/bin/bash
# Set variables
email="test@gmail.com"
subject="I will always be here for PLD"

# Send POST request with variables in body
curl -s -X POST -d "email=$email&subject=$subject" $1

