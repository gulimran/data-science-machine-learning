# Loops

def newline():
    print ' '

# For loop with range of numeric numbers
# The , at the end means do not print newline
for x in range(10):
    print x,
newline()
    
# For loop with continue and break in a loop
for x in range(10):
    if (x is 1):
        continue
    if (x > 5):
        break
    print x,
newline()
       
# While loop
x = 0
while (x < 10):
    print x,
    x += 1