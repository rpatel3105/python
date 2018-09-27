#!/bin/python3

import math
import os
import random
import re
import sys
n, d = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

for i in range(d):
    temp=arr.pop(0)
    arr.append(temp)
print(*arr,end=' ')

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))