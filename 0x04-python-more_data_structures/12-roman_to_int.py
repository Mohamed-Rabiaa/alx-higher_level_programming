#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    n = 0
    str_len = len(roman_string)
    if str_len == 0:
        return 0

    roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                 'M': 1000}

    for i in range(str_len):
        if roman_string[i] in roman_dic:
            if i != str_len - 1 and roman_dic[roman_string[i]] <\
               roman_dic[roman_string[i + 1]]:
                n -= roman_dic[roman_string[i]]
            else:
                n += roman_dic[roman_string[i]]

        else:
            return 0

    return n
