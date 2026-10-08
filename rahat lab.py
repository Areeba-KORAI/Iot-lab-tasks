total_marks = 0
max_marks_per_subject = 100
total_possible_marks = 5 * max_marks_per_subject
for i in range(1, 6):
    marks = float(input(f"Enter marks for subject {i}: "))
    total_marks += marks
percentage = (total_marks / total_possible_marks) * 100
if percentage >= 85:
    grade = 'A+'
elif percentage >= 75:
    grade = 'A'
elif percentage >= 65:
    grade = 'B'
elif percentage >= 50:
    grade = 'C'
else:
    grade = 'F'

if grade != 'F':
    status = "Pass"
else:
    status = "Fail"

print("\n--- Result Summary ---")
print(f"Total Marks: {total_marks} / {total_possible_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(f"Status: {status}")