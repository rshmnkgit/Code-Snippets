#!/bin/python3

import math
import os
import random
import re
import sys

def maxHourglassSum(numArr):
    sumarr = []
    hgsum = 0
    for i in range(0,len(numArr)-2):
        for j in range(0, len(numArr)-2):
            hgsum = numArr[i][j] + numArr[i][j+1] + numArr[i][j+2] + numArr[i+1][j+1] + numArr[i+2][j] + numArr[i+2][j+1] + numArr[i+2][j+2]
            sumarr.append(hgsum)
    maxsum=max(sumarr)    
    return maxsum

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(maxHourglassSum(arr))
