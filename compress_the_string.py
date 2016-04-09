from __future__ import print_function
from itertools import groupby

groups = []
data = raw_input()

# groupby() will return once for each group of adjacent characters that are equal
for k, g in groupby(data):
	# k contains the iterated character.  No need to capture it
	# g is a list containing character k iterated  e.g. ['a', 'a', 'a']

	# Store the first group of characters as a list
    groups.append(list(g))


# Output the group in the desired format
for k in groups:
	# Implement the output formatting requirements
	print ("(", len(k), ", ", k[0], ") ", sep="", end = "")

# Close with a new line character
print ("\n", end = "")