#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(n,p):
    k =[]
    for x in range(1,n+1):
        for i in range(n):
            if(p[p[i]-1]==x):
                k.append(i+1)
    return k
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(n,p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

