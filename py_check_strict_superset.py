A = set(raw_input().split())

B = set()
for i in range(int(raw_input())):
	# Union set B with set input
	B |= set(raw_input().split())

# Print "True" if A contains B and A - B is not empty
print A >= B and bool(len(A.difference(B)))
	