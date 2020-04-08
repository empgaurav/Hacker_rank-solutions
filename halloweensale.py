#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    if(p>s):
        return 0
    elif(s-p<p-d):
        return 1
    count = 0
    value = p
    while(1):
        if(p<=m):
            break;
        else:
            value = value + (p-d)
            p = p-d
            count +=1
    value = value - p
    s = s-value

    count += int(s/m)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
