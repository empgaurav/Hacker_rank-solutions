#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    co = 0
    cp = 0
    cn= 0
    # fp = 0.0000
    # fn = 0.0000
    # fo = 0.0000
    for i in range(len(arr)):
        if(arr[i]>0):
            cp+=1
        elif(arr[i]<0):
            cn+=1
        else:
            co+=1
    print(cp/len(arr))
    print(cn/len(arr))
    print(co/len(arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)




