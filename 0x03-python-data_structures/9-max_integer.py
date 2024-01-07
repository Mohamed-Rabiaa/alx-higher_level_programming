#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    i, max_num = 0, 0
    length = len(my_list)
    while i < length:
        if my_list[i] > max_num:
            max_num = my_list[i]
        i += 1
    return max_num
