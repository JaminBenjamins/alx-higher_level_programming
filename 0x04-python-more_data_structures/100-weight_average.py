#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    den = 0

    for w in my_list:
        num += w[0] * w[1]
        den += w[1]
    return (num / den)
