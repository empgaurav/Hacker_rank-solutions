#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    if(n==0):
        print(1)
    height = 1
    for i in range(1,n+1):
        if(i%2!=0 and n>1):
            height = height*2;
        else:
            height +=1;
    return height

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
