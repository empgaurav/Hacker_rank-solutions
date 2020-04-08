#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    m = 1
    if(n == 0):
        print(1)
    for i in range(1,n+1):
        m = m * i
    print(m)


if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
