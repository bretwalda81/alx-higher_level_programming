#!/bin/bash
# This script takes in the given URL and displays all allowed HTTP methods on the server
curl -si -X OPTIONS "$1" | grep 'Allow' | cut -d ' ' --complement -f1
