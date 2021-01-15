def format_number_as_percentage():
    x = 0.25
    y = -0.25
    print("\nOriginal Number: ", x)
    print("Formatted Number with percentage: "+"{:.2%}".format(x));
    print("Original Number: ", y)
    print("Formatted Number with percentage: "+"{:.2%}".format(y));
    print()

format_number_as_percentage()