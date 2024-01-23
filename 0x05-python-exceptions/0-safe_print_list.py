#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed_items_counter = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            printed_items_counter += 1
    except IndexError:
        pass
    finally:
        print()
        return printed_items_counter
