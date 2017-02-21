# Declare a list
x = [1, 2, 3, 4, 5, 6]

# Size of a list
print len(x)

# First three elements of a list
print x[:3]

# Start from index three and to the end - elements of a list
print x[3:]

# Last two elements of a list
print x[-2:]

# Add elements of another list to a given list
x.extend([7,8])
print x

# Add a single element into a given list
x.append(9)
print x

# List containing lists as elements
y = [10, 11, 12]
listOfLists = [x, y]
print listOfLists

# Get an element of a list at a given index
print y[1]

# Sort a list
z = [3, 2, 1]
z.sort()
print z

# Sort a list in reverse order
z.sort(reverse=True)
print z