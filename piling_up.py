from collections import deque


for _ in range(int(raw_input())):
	#Grab size of deque
	raw_input()
	
	#Grab the set deque of cubes
	test_case = deque(map(int, raw_input().split()))

	result = 'Yes'
	top = max(test_case[0], test_case[-1])

	while len(test_case) > 0:
		if test_case[0] == top:
			#if left cube equals top cube, pop left
			top = test_case.popleft()
		elif test_case[-1] == top:
			#if right cube equals top cube, pop right
			top = test_case.pop()
		elif top > max(test_case[0], test_case[-1]):
			#if top is bigger than larger of left and right cube
			top = max(test_case[0], test_case[-1])
		else:
			#top is not bigger than the larger of left and right cube
			result = 'No'
			break
		
	print result