#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    len = len(argv)
    if len == 1:
        print(0)
    else:
        sum = 0
        for i in range(1, len):
            sum += int(argv[i])
        print(sum)
            
