def format_number_as_percentage():
    x = 0.25
    y = -0.25
    print("\nOriginal Number: ", x)
    print("Formatted Number with percentage: "+"{:.2%}".format(x))
    print("Original Number: ", y)
    print("Formatted Number with percentage: "+"{:.2%}".format(y))
    print()


from numpy import prod
def find_difference(a, b):
    return abs(prod(a) - prod(b))

from operator import mul
from functools import reduce
def find_difference(a, b):
    return abs(reduce(mul, a) - reduce(mul, b))

find_difference = lambda a,b,p=__import__("numpy").prod: abs(p(a)-p(b))

find_difference = lambda (a, b, c), (x, y, z): abs(a * b * c - x * y * z)

from numpy import prod
find_difference = lambda a, b: abs(prod(a) - prod(b))

format_number_as_percentage()