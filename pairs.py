#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    brr = set(arr)
    count = 0
    for i in range(len(arr)):
        if( (arr[i]-k) in brr):
            count+=1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
