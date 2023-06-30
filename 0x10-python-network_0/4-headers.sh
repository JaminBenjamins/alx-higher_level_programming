#!/bin/bash
#takes in a URL as argument sends a GET request 
# and display body of response
curl -sH "X-School-User-Id: 98" "$1"
