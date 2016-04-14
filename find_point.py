def get_int():
	while True:
		try:
			X = int(raw_input())
			break
		except:
			print "Input could not be converted to an integer.  Try again"
			continue
	return X
 
def get_coords():
	while True:
		try:
			input = raw_input().split()
			output = map(int, input)
			break
		except:
			print "Input could not be converted to an integer.  Try again"
			continue
	return output
 
N = get_int()
coord_array = []


for n in range(N):
	coord_list = get_coords()
	coord_array.append(coord_list)

for n in coord_array:
	dy = n[3] - n[1]
	dx = n[2] - n[0]
	y = n[3] + dy
	x = n[2] + dx

	print x, y

