#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    count = 0
    if arr:
        small_stick = min(arr)
    else:
        return
    new_sticks = []
    for element in arr:
        count = count + 1
        new_element = element - small_stick
        if new_element != 0:
            new_sticks.append(new_element)
    print(count)
    cutTheSticks(new_sticks)
        
  

if __name__ == '__main__':
   
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

   
