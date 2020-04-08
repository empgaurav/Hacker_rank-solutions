#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    bob=0
    alice = 0
    result = []
    for i in range(len(a)):
        if a[i]>b[i]:
            alice +=1
        elif a[i]<b[i]:
            bob +=1
    result.append(alice)
    result.append(bob)
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()



"""###############################   TEST CASE###############
INPUT
5 6 7
3 6 10
OUTPUT
1 1
"""###########################################################
