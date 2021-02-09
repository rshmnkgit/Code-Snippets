def nb_year(p0, percent, aug, p):
    # your code
    no_years = 0
    pop = p0
    while pop < p:
        pop = pop + (pop * percent/100) + aug
        no_years = no_years + 1
    return no_years

def is_isogram(string):
    return len(string) == len(set(string.lower()))


def is_isogram(string):
    #your code here
    string = string.lower()
    for s in string:
        if (string.count(s) > 1):
            return False
    return True

    
is_isogram("jtyfytytfjgyftyfytgyjgyh")


print(nb_year(1500, 5, 100, 5000))
print(nb_year(1500, 5, 100, 5000), 15)
print(nb_year(1500000, 2.5, 10000, 2000000), 10)
print(nb_year(1500000, 0.25, 1000, 2000000), 94)
print(nb_year(1500000, 0.25, -1000, 2000000), 151)
print(nb_year(1500000, 0.25, 0, 2000000), 116)
print(nb_year(1500000, 0.0, 10000, 2000000), 50)