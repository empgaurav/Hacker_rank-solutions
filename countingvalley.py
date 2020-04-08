#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    c = []
    sumval = 0
    count = 0
    for i in s:
        if i=='D':
            c.append(-1)
        else:
            c.append(1)
    for i in range(len(c)):
        sumval += c[i];
        if(sumval==0 and c[i]==1):
            count +=1;
    return count 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
