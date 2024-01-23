#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res_list = []
    for i in range(list_length):
        try:
            res_list += [my_list_1[i] / my_list_2[i]]
        except TypeError:
            res_list += [0]
            print("wrong Type")
        except ZeroDivisionError:
            res_list += [0]
            print("division by 0")
        except IndexError:
            res_list += [0]
            print("out of range")
        finally:
            continue
    return res_list
