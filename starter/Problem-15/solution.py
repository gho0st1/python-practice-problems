'''
Problem-15: Write conditional statements to identify the student’s average marks. If any subject’s mark is less than 40, you should print FAILED instead of making average marks
	lstudent_1 = [40, 35, 70, 90, 56]
	student_2 = [57, 35, 80, 98, 46]
'''

student_1 = [40, 35, 70, 90, 56]
student_2 = [57, 54, 71, 98, 46]

def calculate_result(marks: list[int]) -> str:
	if (any(mark < 40 for mark in marks)):
		return "FAILED"
	else:
		return "Average marks - " + format(sum(marks) / len(marks), ".2f")
	
print("Result of Student_1:", calculate_result(student_1))
print("Result of Student_2:", calculate_result(student_2))