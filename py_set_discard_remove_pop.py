def get_int():
	return int(raw_input())

def get_set():
	"""Prompts user for space-sparated set of integers"""
	while True:
		try:
			S = raw_input().split()
			S = set(map(int, S))
			break
		except:
			print "Input must be integers"
			continue
	return S

def get_command():
	"""Prompts user for a stack operation
	   Returns the stack operation as a list"""
	S = raw_input().split()

	try:
		# input contains a command and value
		return [S[0], int(S[1])]
	except:
		# input contains a command and no value
		return S

def process_commands(input_set, commands):
	"""input_set = set of integers to process
	   commands = stack of commands to process against input set"""
	# Process commands
	while len(commands) > 0:
		C = commands.pop(0)
		if C[0] == 'pop':
			input_set.pop()
		elif C[0] == 'remove':
			input_set.remove(C[1])
		elif C[0] == 'discard':
			input_set.discard(C[1])
		else:
			break
	return input_set

# Get the number of elements in the set
get_int() # we will discard this input

# Get the set of integers
input_set = get_set()

# Get commands
commands = []
for x in range(0, get_int()):
	commands.append(get_command())

result_set = process_commands(input_set, commands)

print sum(result_set)
