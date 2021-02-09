
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

for i in range(10):
    print(fibonacci1(i))