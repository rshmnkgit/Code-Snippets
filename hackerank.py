
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

# Print Even and odd positioned letters in a string
def oddevens():
    ntest = int(input())
    input_string = []
    for i in range(0,ntest):
        input_string.append(input())


    for t in range(0,ntest):
        mystr = input_string[t]
        evens =''
        odds = ''
        for i in range(0, len(mystr)):
            if (i%2):
                odds = str(odds) + str(mystr[i])   #odds.join(mystr[i])
            else:
                evens = str(evens) + str(mystr[i])
        print(f"{evens} {odds}")


def count_substring(string, sub_string):
    found = True
    count = 0
    l = len(sub_string)
    mystr = string

    while (found==True):
        found=False
        # print(found)
        p = mystr.find(sub_string)
        print(p)
        if (p >=0):
            found=True
            count += 1
            mystr = mystr[p+l:]
        else:
            found=False
            break
        print(mystr)
            
    return count

  
# string.isalnum()  This method checks if all the characters of a string are alpha-numeric (A_Z / a-z / 0-9).
# string.isalpha()  This method checks if all the characters of a string are alphabets (A_Z / a-z).
# string.isdigit()  This method checks if all the characters of a string are numeric (0-9).
# string.islower()  This method checks if all the characters of a string are in lowercas (a-z).
# string.isupper()  This method checks if all the characters of a string are in uppercase (A_Z).

def charsInString():
    s = input()
    al = an = dg = lr = up = False
    for ch in s:
        if(ch.isalnum()):
            al = True
        if(ch.isalpha()):
            an = True
        if(ch.isdigit()):
            dg = True
        if(ch.isupper()):
            up = True
        if(ch.islower()):
            lr = True
    print(f"{al}\n{an}\n{dg}\n{lr}\n{up}")

    # Same as above using any() 
    print(any([char.isalnum() for char in s]))
    print(any([char.isalpha() for char in s]))
    print(any([char.isdigit() for char in s]))
    print(any([char.islower() for char in s]))
    print(any([char.isupper() for char in s]))


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # a = list(map(int, input().rstrip().split()))
    # b = list(map(int, input().rstrip().split()))
    # result = compareTriplets(a, b)
    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()

    # arr = list(map(int, input().rstrip().split()))

    # print(amIOld(16))
    # print(amIOld(19))
    # print(amIOld(10))
    # print(amIOld(12))
    # print(amIOld(17))