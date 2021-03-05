import math
def addTwoDigits(n):
    nsum = 0
    number = n
    while (number>0):
        digit = number%10
        nsum = nsum+digit
        number = number//10
        print(f"{nsum}   {digit}   {number} ")
    return sum

def centuryYear(year):
    return (math.ceil(year/100))


def adjacentElementsProduct(inputArray):
    maxProd = 0
    for i in len(inputArray):
        prod = inputArray[i] * inputArray[i+1]
        if prod > maxProd:
            maxProd = prod
    return maxProd


def almostIncreasingSequence(sequence):
    arr = set(sequence)
    print (arr)
    if len(arr)<len(sequence)-1:
        print(False)
    else:
        print(True)
    # return False if count>1 else True

    

# print([2,1,3,4])

arr = [1,1,2, 3,4,4]
print(almostIncreasingSequence(arr))

# # inputNumber = int(input())
# # print(inputNumber)
# print(addTwoDigits(67))
# year = 1902
# print(centuryYear(year))