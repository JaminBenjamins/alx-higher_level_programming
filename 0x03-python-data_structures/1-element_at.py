#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list) - 1:
        return None
    for i in range(my_list):
        idx = my_list[i]
    return idx
