#!/usr/bin/python3
def list_max_value(my_list=[]):
    max_value = my_list[0]
    for i in my_list:
        if i > max_value:
            max_value = i
    return max_value


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    values_list = list(a_dictionary.values())
    max_value = list_max_value(values_list)

    for x, y in a_dictionary.items():
        if y == max_value:
            return x
