# Tuples are just immutable lists. Use () instead of []
x = (1, 2, 3)
print len(x)

# Get an element at a given index
y = (4, 5, 6)
print y[2]

# Tuple containing tuples as elements
listOfTuples = [x, y]
print listOfTuples

# Parsing into tuple
(age, income) = "32,120000".split(',')
print age
print income