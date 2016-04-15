def get_int():
	"""Prompts user for a single integer and converts to a set"""
	while True:
		try:
			print "Enter an integer:"
			x = int(raw_input())
			break
		except:
			continue             
	return x 

def get_set():
	"""Prompts user for set of integers and converts to a set"""
	while True:
		try:
			print "Enter a set of integers:"
			string_in = raw_input().split()
			int_in = map(int, string_in)
			break
		except:
			continue
	return set(int_in)

# Get user input
M = get_int()
M_set = get_set()
N = get_int()
N_set = get_set()

union_set = M_set.union(N_set)
intersection_set = M_set.intersection(N_set)
output_list = list(union_set.difference(intersection_set))

for x in sorted(output_list):
	print x