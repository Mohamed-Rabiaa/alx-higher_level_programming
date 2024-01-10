#!/usr/bin/python3
def number_keys(a_dictionary):
    if not a_dictionary:
        return 0
    keys_list = list(a_dictionary)

    for keys_counter in range(len(keys_list)):
        keys_counter += 1
    return keys_counter
