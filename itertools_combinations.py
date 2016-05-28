from itertools import combinations

X = raw_input()
S, k = list(X.split()[0]), int(X.split()[1])
S.sort()

# Print the output
for i in range(k):
	for j in list(combinations(S, i + 1)):
		print ''.join(j)