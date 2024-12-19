import math

number = 10
square_root = math.sqrt(number)
print(f"The square root of {number} is {square_root}")


# explore the math module

# List all attributes and functions in the math module

# print(dir(math))

# Get detailed information about the math.sqrt function

# help(math.sqrt)


# Wrap the Logic in a Custom Function
def get_root(number):
    import math
    return math.sqrt(number)

# Test the function
print(f'Calling get_root function of {number}: {get_root(number)}')  # Output: 3.1622776601683795


# Create an add_numbers Function:


def add_numbers(a, b):
    total = a + b
    return get_root(total)



# Test the function
print(f'Calling add_numbers function for {number} and 30 : {add_numbers(10, 30)}')  

