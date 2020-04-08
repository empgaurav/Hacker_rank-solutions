#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    mxs = sum(arr[1:])
    mns = sum(arr[0:4])
    print(mns,end = " ")
    print(mxs)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)




"""##################  TEST CASE ###########
INPUT
1 2 3 4 5
OUTPUT
10 14
##########################################"""
