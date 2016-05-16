
def get_int_set ():
	# Prompt user for a set of space-separated integers
	output_int_set = set(map(int, raw_input().split()))
	return output_int_set

def get_set_operation():
	# Prompt user for 1) a set operation 2) a set
	operation = raw_input().split() ##
	operation_set = get_int_set()
	
	return [operation, operation_set]

def run_operation(start_set, operation, modifier_set):
	"""Accepts start set, operation, and modifier_set
	   start_set = set with we are modifying
	   operation = method we are using for the modification.  Accepted values:
					- intersection_update
					- symmetric_difference_update
					- difference_update
	   modifier_set = set we are using to perform the modification"""
	if operation == 'intersection_update':
		#intersection code here
		#print "performing intersection"
		start_set &= modifier_set
	elif operation == 'update':
		#update code here
		start_set |= modifier_set
	elif operation == 'symmetric_difference_update':
		#symmetric difference code here
		#print "perfomring symmetric difference"
		start_set ^= modifier_set
	elif operation == 'difference_update':
		#difference update code here
		#print "performing difference"
		start_set -= modifier_set
	else:
		assert False, "Unexpected operation"

	return start_set


# Get count and elements in set A
set_a_len = raw_input()	# count
set_a = get_int_set()	# elements

# Get count of operations
n = int(raw_input())

# Get the list of operations
operations = []
for i in range(n):
	operations.append(get_set_operation())

for i in operations:
	#print "operation is", i[0][0]
	#print "set is", i[1]
	#print i
	run_operation(set_a, i[0][0], i[1])

print sum(set_a)