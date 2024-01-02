#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        n = ord(str[i])
        if n >= 97 and n <= 122:
            n  = n - 32
        if i != len(str) - 1:
            print(chr(n) , end='')
        else:
            print(chr(n))
