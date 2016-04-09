# Enter your code here. Read input from STDIN. Print output to STDOUT

command_count = int(raw_input())
command_list = []
list = []

for i in range(0, command_count):
	command = raw_input()			# Input command raw input
	command = command.split()		# Store input as a list
	command_list.append(command)	# Append list to command_list to run later

for i in command_list:
	if i[0] == 'insert':
		list.insert(int(i[1]), int(i[2]))

	elif i[0] == 'print':
		print list

	elif i[0] == 'remove':
		list.remove(int(i[1]))	

	elif i[0] == 'append':
		list.append(int(i[1]))
	
	elif i[0] == 'sort':
		list.sort()
	
	elif i[0] == 'reverse':
		list.reverse()
	
	elif i[0] == 'pop':
		list.pop()

	else:
		print 'Command not recognized', i