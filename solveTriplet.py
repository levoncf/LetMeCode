#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    AliceList = [a0, a1, a2]
    BobList = [b0, b1, b2]
    AliceCount = 0
    BobCount = 0
    for i in range(3):
        if AliceList[i] > BobList[i]:
            AliceCount += 1
        elif AliceList[i] < BobList[i]:
            BobCount += 1
        else:
            continue
    return (AliceCount, BobCount)
