
def get_int():
	"""Prompt the user for an integer"""
	while True:
		try:
			X = int(raw_input())
			break
		except:
			print "Could not convert input to integer"
			continue
	return X

def get_fibo(X):
	"""Return a fibonacci sequence that goes to at least value X"""
	fibo_vals = [0, 1]  # Initialize fibonacci set

	while X > max(fibo_vals):
		L = len(fibo_vals)
		N = fibo_vals[L - 1] + fibo_vals[L - 2]
		fibo_vals.append(N)

	return set(fibo_vals)

# Prompt user for input
input_vals = []
nums = get_int()
for i in range(nums):
	n = get_int()
	input_vals.append(n)

# Create a set of fibonacci numbers
X = get_fibo(max(input_vals))

# Return IsFibo for each input_val that is in the fibonacci sequence
for i in input_vals:
	if i in X:
		print "IsFibo"
	else:
		print "IsNotFibo"
