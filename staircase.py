#!/bin/python

import sys


n = int(raw_input().strip())

for y in range(0, n):
	output = ""
	for x in range (0, n):
		# If x is at the starting position of Xs print X
		if x >= n - y - 1:
			output += "#"
		else:
			output += " "
	print output	