from collections import defaultdict

# Collect length of Group A and Group B
A, B = map(int, raw_input().split())
GroupA, GroupB = defaultdict(list), list()

# Collect A words for group A 
for a in range(A):
	GroupA[raw_input()].append(a + 1)

# Collect B words for group B
for b in range(B):
	GroupB.append(raw_input())

# Print the index positions of GroupA for all words in GroupB or a -1
for b in GroupB:
	print (' '.join(map(str, GroupA[b])) or -1)
