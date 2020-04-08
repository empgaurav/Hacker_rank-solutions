#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    sumleft = 0
    total = sum(arr)
    has_equal = False
    for i in range(1, len(arr)):
        sumright = 0
        sumleft += arr[i-1]
        sumright = total - sumleft - arr[i]
        if sumleft == sumright:
            has_equal = True
            break

    if has_equal or len(arr) == 1:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
