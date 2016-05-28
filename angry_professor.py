for K in range(int(raw_input())):
	students_required = int(list(raw_input().split())[1])
	attendance_data = map(int, raw_input().split())
	students_on_time = sum(1 for i in attendance_data if i <= 0)
	if students_on_time >= students_required:
		print 'NO'
	else:
		print 'YES'
