
def fibonacci():
    a=0 
    b=1
    print(a,b, end=" ")
    c=0
    for i in range(0,100):    
        c = a+b
        print (c, end=" ")
        a = b
        b = c


def fibonacci1(n):
    if (n <= 1):
        return n
    else:
        return (fibonacci1(n-1) + fibonacci1(n-2))

import math
def isPrime(n):
    prime = True
    for i in range(2, int(math.sqrt(n))+1):
        if (n%i == 0):
            prime = False
    return prime


def sortArray(arr):
    l = len(arr) + 1
    for i in range(0,l+1):
        print (i, end=" ")
        if (arr[i] > arr[i+1]):
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

print(sortArray([9,3,5,2,7,1,0,4]))


# for x in range(100,200):
#     if isPrime(x):
#         print(x, end=" ")

# for i in range(10):
#     print(fibonacci1(i))