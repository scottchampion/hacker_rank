from collections import OrderedDict


words = OrderedDict()

for i in range(int(raw_input())):
	word = raw_input()
	try: words[word] += 1
	except: words[word] = 1

print len(words)

for word in words:
	print str(words[word]),