#!/bin/bash
#Takes an URL sends a POST request to URL and display body response
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
