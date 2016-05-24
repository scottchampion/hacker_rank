A = set(raw_input().split())
flag = True

for i in range(int(raw_input())):
	if flag == True:
		# Union set B with set input
		B = set(raw_input().split())

		# Print "True" if A contains B and A - B is not empty
		flag = flag and A >= B and bool(len(A.difference(B)))

print flag