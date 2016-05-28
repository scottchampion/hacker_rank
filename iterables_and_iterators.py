from itertools import combinations

N, L, K, l = raw_input(), raw_input().split(), int(raw_input()), 0

for i in list(combinations(L, K)):
	# Check if 'a' is in any combination
	if ''.join(i).find('a') != -1:
		l += 1

print 1.0 * l / len(list(combinations(L, K)))