#!/bin/bash
#A script that sends a request URL and display status code 
curl -s -o /dev/null -w "%{http_code}" "$1"
