# Functions

# Declare a function
def SquareIt(x):
    return x * x

# Call a function
print SquareIt(2)

# Pass functions around as parameters
def DoSomething(f, x):
    return f(x)

print DoSomething(SquareIt, 3)

# Lambda functions let you inline simple functions
print DoSomething(lambda x: x * x * x, 3)