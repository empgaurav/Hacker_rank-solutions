#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    b =[]
    c = []
    for i in range(len(ar)):
        if(ar[i] not in b):
            b.append(ar[i])
            count = ar.count(ar[i])
            count = int(count*0.5)
            c.append(count)
    return sum(c)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
