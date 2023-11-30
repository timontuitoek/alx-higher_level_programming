#!/bin/bash

# Check if the user has provided a URL as a command-line argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the provided URL in a variable
url="$1"

# Send a request to the URL using curl with the -sI option to fetch only the headers
# Then, use grep and awk to extract the size of the response body in bytes from the Content-Length header
response_size=$(curl -sI "$url" | grep -i Content-Length | awk '{print $2}' | tr -d '\r')

# Check if the size of the response body was successfully extracted
if [ -z "$response_size" ]; then
    echo "Failed to get response size from the URL"
else
    echo "Response size: $response_size bytes"
fi
