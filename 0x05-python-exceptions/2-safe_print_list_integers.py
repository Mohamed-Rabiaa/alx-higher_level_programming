#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_items_counter = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            printed_items_counter += 1
        except (ValueError, TypeError):
            pass
    print()
    return printed_items_counter
