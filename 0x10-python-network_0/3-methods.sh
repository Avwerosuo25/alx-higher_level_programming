#!/bin/bash
# display specific HTTP methods acceptable by the server
response=$(curl -sI $1)
