def get_int():
	"""Prompt user for an integer; repeat prompt until entry can map to in"""
	while True:
		try:
			x = int(raw_input())
			break
		except:
			print "Entry must be an integer, try again."
			continue
	return x

def get_list():
	"""Prompt user for space-separated integer list; on error, repeat prompt"""
	while True:
		try:
			string = raw_input().split()
			x = map(int, string)
			break
		except:
			print "List must contain only integers."
			continue
	return x

get_int()

user_input = set(get_list())	# Convert to set to remove duplicate values
user_input = sorted(user_input, None, None, True)	# Reverse-sort de-duped list 

print user_input[1]		# Print the second value
