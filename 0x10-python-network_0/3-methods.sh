#!/bin/bash
# Retrieves the method allowable by the client
curl -sI "$1" | grep "Allow" | cut  -d " " -f 2-
