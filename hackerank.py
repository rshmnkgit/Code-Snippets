
import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    score = [0,0]
    for i in range(0,3):
        if (a[i] > b[i]):
            score[0] += 1
        elif (a[i] < b[i]):
            score[1] += 1
    return score


def miniMaxSum(arr):
    minsum = 0
    maxsum = 0
    for i in range(0,5):
        sum = 0
        for j in range(0,5):
            if (i != j):
                sum += arr[j]
        if (i==0):
            minsum = sum
            maxsum = sum
        else:
            if (sum < minsum):
                minsum = sum
            elif (sum > maxsum):
                maxsum = sum
    print(f"{minsum} {maxsum}");


def amIOld(age):
        # Do some computations in here and print out the correct statement to the console 
        if (age > 18) :
            print("You are old")
        elif (age >=13):
            print("You are a teenager")
        else:
            print("You are young")



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # a = list(map(int, input().rstrip().split()))
    # b = list(map(int, input().rstrip().split()))
    # result = compareTriplets(a, b)
    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()

    # arr = list(map(int, input().rstrip().split()))

    print(amIOld(16))
    print(amIOld(19))
    print(amIOld(10))
    print(amIOld(12))
    print(amIOld(17))