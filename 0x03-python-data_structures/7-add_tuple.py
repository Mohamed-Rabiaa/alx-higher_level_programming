#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_length, b_length = len(tuple_a), len(tuple_b)
    for i in range(2):
        if a_length < 2:
            tuple_a += (0,)
            a_length += 1
        if b_length < 2:
            tuple_b += (0,)
            b_length += 1
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tuple
