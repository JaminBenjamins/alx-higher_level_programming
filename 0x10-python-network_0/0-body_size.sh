#!/bin/bash
# Count the body of an http response
curl -s "$1" | wc -c
