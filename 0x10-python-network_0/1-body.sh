#!/bin/bash

if [ -z "$1" ]; then
 echo "Usage: $0 <URL>"
 exit 1
fi

url=$1
response=$(curl -s -w "%{http_code}" "$url")
status_code=${response: -3}
body=${response::-3}

if [ "$status_code" -eq 200 ]; then
 echo "$body"
else
 echo "Request failed with status code $status_code"
fi