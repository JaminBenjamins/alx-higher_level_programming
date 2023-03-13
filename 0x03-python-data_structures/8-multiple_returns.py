#!/usr/bin/python3
def multiple_returns(sentence):
    tuple = ()
    if sentence == 0:
        tuple = 0, None
    else:
        tuple = (len(sentence), sentence[0]) 
