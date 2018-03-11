#!/bin/python3

import sys

def plusMinus(arr):
    # Complete this function
    pos = 0
    neg = 0
    zero = 0

    for i in arr:
        if i > 0:
            pos = pos + 1
        elif i < 0:
            neg = neg + 1
        else:
            zero = zero + 1
    print (pos/n)
    print (neg/n)
    print (zero/n)

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)
