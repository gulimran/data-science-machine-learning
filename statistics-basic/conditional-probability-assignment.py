# Assignment
#
# Modify the code such that the purchase probability does NOT vary with age, 
# making E and F actually independent.
#
# Then, confirm that P(E|F) is about the same as P(E), showing that the 
# conditional probability of purchase for a given age is not any different 
# than the a-priori probability of purchase regardless of age.

# This computes conditional probability regarding how much stuff people 
# purchase given their age range. We generate 100,000 random people and randomly
# assigns them as being in their 20's, 30's, 40's, 50's, 60's, or 70's.
#
# We assign a lower probability for young people to buy stuff.
#
# We have two Python dictionaries:
#    1. "totals" contains the total number of people in each age group
#    2. "purchases" contains the total number of things purchased by people in each age group
#
# The grand total of purchases is in totalPurchases

from numpy import random

random.seed(0)

totals = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
purchases = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
totalPurchases = 0

for _ in range(100000):
    ageDecade = random.choice([20, 30, 40, 50, 60, 70])
    purchaseProbability = random.random()
    totals[ageDecade] += 1
    
    if (random.random() < purchaseProbability):
        totalPurchases += 1
        purchases[ageDecade] += 1
        
print "Total people: ", totals
print "Purchases: ", purchases
print "Total purchases: ", totalPurchases

# conditional probability
# compute P(E|F), where E is "purchase" and F is "person in 30's"
# The probability of someone in their 30's buying something is the percentage 
# of how many 30-year-olds bought something:

PEF = float(purchases[30]) / float(totals[30])
print "P(purchase | 30s): ", PEF

# P(F) is the probability of being 30 in this data set:

PF = float(totals[30]) / 100000.0
print "P(30's): ", PF

# P(E) is the overall probability of buying something, regardless of the age:

PE = float(totalPurchases) / 100000.0
print "P(Purchase):", PE

# If E and F were independent, then we would expect P(E | F) to be about the same
# as P(E). But they're not; PE is 0.45, and P(E|F) is 0.3. So, that tells us that
# E and F are dependent (which we know they are in this example.)

# P(E)P(F) is P(E) * P(F)

print "P(30's)P(Purchase)", PE * PF

# P(E,F) is different from P(E|F). 
# P(E,F) would be the probability of both being in your 30's and buying something, 
# out of the total population - not just the population of people in their 30's:

print "P(30's, Purchase)", float(purchases[30]) / 100000.0

# P(E,F) = P(E)P(F) but because E and F are dependent on each other and because 
# of the randomness of the data we have, it's quite close but not the same.

# P(E|F) = P(E,F)/P(F)
print "P(30s | Purchase)", (float(purchases[30]) / 100000.0) / PF