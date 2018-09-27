#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(array):
    l=[]
    b=[]
    for k in range(4):
        l = []
        l.append(array[0][0 + k:3 + k])
        l.append(array[1][1 + k])
        l.append(array[2][0 + k:3 + k])
        b.append(sum(sum(x) if isinstance(x, (list, tuple)) else x for x in l))
        
        for j in range(4):
            for i in range(4):
                l=[]
                l.append(array[0][0+i:3+i])
                l.append(array[1][1+i])
                l.append(array[2][0+i:3+i])
                b.append(sum(sum(x) if isinstance(x,(list,tuple)) else x for x in l))

        del(array[0])
    return max(b)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
