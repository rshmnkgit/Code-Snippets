def DNA_strand(dna):
    str = ""
    for i in range(0, len(dna)):
        if dna[i] == 'A':
            code = 'T'
        elif dna[i] == "T":
            code = 'A'
        elif (dna[i] == 'C'):
            code = 'G'
        elif (dna[i] == 'G'):
            code = 'C'
        str = str + code
    return str


def get_sum(a,b):
    #good luck!
    if (a == b):
        return a
    else:
        sum = 0
        for i in range(a,b+1):
            sum = sum + i
        return sum


from fractions import Fraction
def printer_error(s):    
    # your code
    l = len(s)
    count = 0
    for i in range(0, l):
        if s[i] > 'm' and s[i] <= 'z':
            count = count + 1
    s = f'{count}/{l}'
    return s


def find_even_index(arr):
    sum_left = 0
    sum_right = 0
    idx = -1
    for i in range(0, len(arr)):
        sum_right = 0
        for j in range(i+1, len(arr)):
            sum_right = sum_right + arr[j]
        if sum_left == sum_right:
            idx = i 
            break
        else:
            sum_left = sum_left + arr[i]
    return idx

def find_even_index_1(arr):
    for i in range(len(arr)):
        if sum(arr[i:]) == sum(arr[:i+1]):
           return i
    return -1

def filter_list(l):
    lst = []
    for i in l:
        if type(i) != str:
            lst.append(i)
    return lst

def filter_list_1(l):
    #return a new list with the strings filtered out
    return [x for x in l if type(x) is not str]

def filter_list_2(l):
    #return a new list with the strings filtered out'
    return [i for i in l if not isinstance(i, str)]




def longest(s1,s2):
    c = s1+s2
    c = set(c)
    c = ''.join(sorted(c))
    print(c)
    return c

# print(list('fgfdhghff'))
res=[]
res[:] = "fgfdhghff"
# print(res)
print(set("hhhhhmmmmm"))
print(longest('apppsffsagfsfdsfaaah', 'ggrregererh'))

# print(filter_list([1,2,'a','b', 6, 9, 'brerberb',29.8]))

r = sum(range(10))
print(r)


# Activity 4 - Even Arrays - Find the index of the item where  
# the sum of the numbers to the left of that index = sum of the numbers to the right of that index
# [1,2,3,4,3,2,1]
# myArray = [20,10,-80,10,10,15,35]
# myArray = [10,-80,10,10,15,35,20]
# getIndex = find_even_index(myArray)
# print(getIndex)


# # Ativity 3 - printer color code error
# strColor = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
# error = printer_error(strColor)
# print(f'error:  {error}')

# # Activity 2 - Sum of integers between two numbers including the two numbers
# sumnum = get_sum(2,4)
# print(sumnum)

# # Activity 1 - DNA 
# dstrand = DNA_strand('AGCTATCGAT')
