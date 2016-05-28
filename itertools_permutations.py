from itertools import permutations

X = raw_input()
S, k = list(X.split()[0]), int(X.split()[1])
S.sort()

# Print the output
for i in list(permutations(S, k)):
	print ''.join(i)
