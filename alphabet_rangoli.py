
def get_line(line, N):
	"""Return a list of characters for a given line of a rangoli of size N""""
	L = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

	line_str = []
	y = 0			# This is super-hacky, but works; clean-up later 
	for x in range(N):
		if x < N - line - 1:
			line_str.append('-')
		else:
			line_str.append(L[N - y - 1])
			y += 1	

	output = list(line_str)
	line_str.pop()
	line_str.reverse()
	return output + line_str


def print_rangoli(start, N):
	"""Print a rangoli of size 'N' starting from line 'start' """
	# get a list of chars for the line
	line = get_line(start, N)
	
	# print the list of chars separated with '-'
	print '-'.join(line)

	# If the current line is smaller than the total size, increment start and print again
	if start < N - 1:
			print_rangoli(start + 1, N)
	
	# print the list of chars separated with '-'
	if start + 1 == N:
		return
	else:
		print '-'.join(line)

def get_int():
	while True:
		try:
			x = int(raw_input())
			break
		except:
			print "Could not convert input to integer.  Try again"
			continue
	return x

x = get_int()
print_rangoli(0, x)

