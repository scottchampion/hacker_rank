from itertools import product

K = map(int, raw_input().split())
M, K = K[1], K[0]

#  Prompt user for K lists
L = []
for i in range(K):
	L.append(map(int, raw_input().split()[1:]))  # Use [1:] to drop first num 

mod_max = 0
for j in list(product(*L)):
	# Calculate the sum of squares in current list
	line_sum = 0
	for element in j:
		line_sum += element**2 
	
	# Store larger of current sum of squares or current mod_max
	mod_max = max(line_sum % M, mod_max)

print mod_max