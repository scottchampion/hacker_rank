from collections import Counter
from operator import itemgetter

S = raw_input()
character_counter = Counter()

for s in S:
	character_counter[s] += 1


#####################
Out = character_counter.most_common(3)
Sorted_Out = []

Sorted_Out.append(Out.pop(0))

while len(Out) > 0:
	if Out[0][1] == Sorted_Out[-1][1]:
		# if 
		Sorted_Out.append(Out.pop(0))
	else:
		# print and purge content of Sorted_Out
		Sorted_Out.sort(key=lambda x: x[0])
		for i, j in Sorted_Out:
			print i, j
		Sorted_Out = []
		# Load Sorted Out with next value from Out
		Sorted_Out.append(Out.pop(0))

Sorted_Out.sort(key=lambda x: x[0])
for i, j in Sorted_Out:
	print i, j
