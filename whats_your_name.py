first = raw_input()
last = raw_input()

assert len(first) <= 10
assert len(last) <= 10

print "Hello %s %s! You just delved into python." % (first, last)