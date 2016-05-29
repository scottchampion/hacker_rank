from collections import namedtuple

count_students = int(raw_input())

# Create a data type "Student" using list of user-entered parameters
Student = namedtuple('Student',raw_input().split())

Students = []
for i in range(count_students):
	# Convert user input to a "Student" data type
	line = Student(*raw_input().split())
	
	# Append list of Students with user-entered data
	Students.append(line)

# Assume we have a user-entered parameter called "MARKS"
# Sum the MARKS for all students
sum_marks = int(0)
for Student in Students:
	sum_marks += int(Student.MARKS)

# Print the average to 2 decimal places
print '%.2f' % (1.0 * sum_marks / count_students)
