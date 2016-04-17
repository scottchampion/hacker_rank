S = raw_input()
L = ""

# Seems like a weak implementation, but this method does not strip space chars
for char in range(len(S)):
	if char == 0:
		L = L + S[char].upper()
	elif S[char - 1] == ' ':
		L = L + S[char].upper()
	else:
		L = L + S[char]

print L


# This implementation strips spaces
# import string
# S = raw_input()
# print string.capwords(S)