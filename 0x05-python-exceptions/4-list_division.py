#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res_list = []
    temp = 0
    for i in range(list_length):
        try:
            temp = my_list_1[i] / my_list_2[i]
        except TypeError:
            temp = 0
            print("wrong Type")
        except ZeroDivisionError:
            temp = 0
            print("division by 0")
        except IndexError:
            temp = 0
            print("out of range")
        finally:
            pass
        res_list.append(temp)
    return res_list
