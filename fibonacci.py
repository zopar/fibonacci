#!/usr/bin/env python3
"""[summary]

Returns:
    [type]: [description]
"""
# We use a generator
def fibonacci(number):
    """[summary]

    Args:
        number ([type]): [description]

    Returns:
        [type]: [description]
    """
    
    # a is a small cache, we sum based on it
    a=[0,1]
    for i in range(0, number):
        if i == 0:
            yield i
        elif i == 1:
            yield i
        else:
            a[0] = a[0]+a[1]
            yield a[0]
            # We need inversion because we sum always on first element
            a[0], a[1] = a[1], a[0]
        

def to_file(result):
    pass

def main():
    """[summary]
    """
    print("This software prints fibonacci numbers in a file")

    # Manage exception value error if a non numeric value is passed
    try:
        number = int(input("Enter a positive number: "))
    except ValueError:
        print("ERROR: Non-numeric values are not allowed")
        exit(1)

    # Be sure that the passed number is not negative
    if number < 0:
        print("ERROR: Negative values are not allowed")
        exit(1)
        
    # looping over generator, this not increase time complexity     
    for k in fibonacci(number):
        print(k)

if __name__ == "__main__":
    main()
