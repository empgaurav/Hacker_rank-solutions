#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    mini = min(brr)
    answer = []

    lis = [0 for x in range(102)]

    for k in arr:
        lis[k-mini] -= 1
    for d in brr:
        lis[d-mini] += 1

    for ind, ele in enumerate(lis):
        if ele != 0:
            answer.append(ind+mini)
    return answer
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
