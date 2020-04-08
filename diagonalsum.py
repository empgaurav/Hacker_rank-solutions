#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    ld= []
    rd= []
    res = 0
    for i in range(n):
        ld.append(arr[i][i])
    for i in range(n):
        rd.append(arr[i][len(arr)-i-1])
    res = abs(sum(ld)-sum(rd))
    return res
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()



"""######################### TEST CASE ###########
INPUT
3
11 2 4
4 5 6
10 8 -12
OUTPUT
15
##############################################"""
