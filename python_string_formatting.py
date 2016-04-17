N = int(raw_input())

# Set L to the length of the binary format of N
L = len(format(N, 'b'))

for i in range(1, N + 1):
	dec = format(i, 'd').rjust(L)
	oct = format(i, 'o').rjust(L)
	hex = format(i, 'X').rjust(L)
	bin = format(i, 'b').rjust(L)

	print dec, oct, hex, bin
