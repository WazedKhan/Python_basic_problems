#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def compareTriplets(a, b):
    arr = [0, 0]
    for i in range(len(a)):
        if a[i] > b[i]:
            arr[0] = arr[0]+1
        if a[i] < b[i]:
            arr[1] = arr[1]+1
    return arr

# copy


def compareTriplets1(a, b):
    for i in range(len(a)):
        a[i], b[i] = a[i] > b[i], a[i] < b[i]
    return [sum(a), sum(b)]


a = [1, 2, 3]

b = [3, 2, 1]

result = compareTriplets1(a, b)
print(result)
