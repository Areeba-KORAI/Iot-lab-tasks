students = ["Ali", "Ahmed", "Sara", "Ayesha", "Bilal"]

entered_name = input("Enter a student name to search: ")

if entered_name in students:
    print("Student Found")
else:
    print("Student Not Found")