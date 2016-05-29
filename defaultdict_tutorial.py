from collections import defaultdict

# Collect length of Group A and Group B
A, B = map(int, raw_input().split())
GroupA, GroupB = defaultdict(list), list()

# Collect A words for group A 
i = int(1)
for a in range(A):
	GroupA[raw_input()].append(i)
	i += 1

# Collect B words for group B
for b in range(B):
	GroupB.append(raw_input())

# Print the index positions of GroupA for all words in GroupB
for b in GroupB:
	# print -1 if b is not listed in GroupA
	if len(GroupA[b]) < 1:
		print '-1'
	# print space-separated list of indexes in GroupA 
	else:
		print ' '.join(map(str, GroupA[b]))
