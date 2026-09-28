# Student Result Processor

student_name = input("Enter Student Name: ")
student_id = input("Enter Student ID: ")
student_course = input("Enter Student Course: ")
student_year = input("Enter Student Year: ")

mark1 = float(input("Enter Mark 1 (0-100): "))
mark2 = float(input("Enter Mark 2 (0-100): "))
mark3 = float(input("Enter Mark 3 (0-100): "))

marks = [mark1, mark2, mark3]

total = sum(marks)
average = total / len(marks)

if average >= 70:
    result = "Distinction"
elif average >= 50:
    result = "Pass"
else:
    result = "Fail"

print("\n===== STUDENT REPORT =====")
print("Student Name :", student_name)
print("Student ID   :", student_id)
print("Student Course :", student_course)
print("Student Year   :", student_year)
print("Marks        :", marks)
print("Total Marks  :", total)
print("Average      :", round(average, 2))
print("Result       :", result)