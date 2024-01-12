#!/usr/bin/python3
def weight_average(my_list=[]):
    wt_sum = 0
    t_total = 0

    for my_tuple in my_list:
        wt_sum += (my_tuple[0] * my_tuple[1])
        t_total += my_tuple[1]

    return wt_sum / t_total
