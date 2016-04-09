# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

input = raw_input()
input_string, char_count = input.split()
input_string = sorted(input_string)
char_count = int(char_count)

# Store combinations of 'input_string choose char_count' in combos variable
combos = list(combinations_with_replacement(input_string, char_count))

for l in combos:
	# Initialize the line as null
	line = ''
	
	# Add the character to the line
	for c in l:
		line += c
	
	# Print the line as a string of characters
	print line