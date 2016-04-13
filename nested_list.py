def get_int():
	""" Prompt user for integer, repeat if given non-int input """
	while True:
		try:
			x = int(raw_input())
			break
		except:
			print "Could not convert input to integer, try again."
			continue
	return x

def get_name():
	""" Prompt user for student name """
	return raw_input()

def get_score():
	while True:
		try:
			x = float(raw_input())
			break
		except:
			print "Could not convert input to float, try again."
			continue
	return x

def second_lowest(input):
	""" Receive a list of student, score pairs; return lowest score """
	scores = []

	# Put the scores into a list
	for student in input:
		scores.append(student[1])
	
	# Convert scores to set then back to list to remove duplicates
	unique_scores = list(set(scores))
	
	if len(unique_scores) == 1:
		# If there is only one student, return his score
		return unique_scores[0]
	else:
		unique_scores = sorted(unique_scores)
		return unique_scores[1]


def students_w_score(students, score):
	""" Receives a list of students and score, returns list of students with score """
	matches = []
	for student in students:
		if student[1] == score:
			matches.append(student[0])

	return sorted(matches)

N = get_int()

students = []
for x in range(N):
	name = get_name()
	score = get_score()
	students.append([name, score])
	#students.append(['F', score])
sec_lowest_score = second_lowest(students)
students_w_score = students_w_score(students, sec_lowest_score)

for student in students_w_score:
	print student