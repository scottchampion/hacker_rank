from collections import OrderedDict

# Use OrderedDict to iterate through words in order entered
words = OrderedDict()

# Prompt user for number of words to expect
for i in range(int(raw_input())):
	word = raw_input()
	# Add word to dictionary; set count = 1 if cannot increment existing count
	try: words[word] += 1
	except: words[word] = 1

# Print count of unique words in dictionary
print len(words)

for word in words:
	print str(words[word]),