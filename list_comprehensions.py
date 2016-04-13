def get_int():
	""" Returns the integer entered by user, repeats if not integer """
	while True:
		try:
			x = int(raw_input())
			break
		except:
			print "Input could not be converted to an integer.  Try again"
			continue
	return x

X = get_int()
Y = get_int()
Z = get_int()
N = get_int()

output_list = []

for x in range(X + 1):
	for y in range(Y + 1):
		for z in range(Z + 1):
			# Only allow combinations whose sum does not equal N
			if x + y + z != N:
				output_list.append([x, y, z])

print output_list
