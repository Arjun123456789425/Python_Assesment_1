student_name = "Arjun"
student_id = "6789"
age = 24
student_marks = [34, 56, 92, 78, 79]
subject_names = ["Maths", "Physics", "Chemistry", "Computer science", "English"]
student = dict(zip(subject_names, student_marks))

total = sum(student_marks)
avg = total / len(student_marks)

highest_mark = max(student_marks)
lowest_mark = min(student_marks)
print("Highest:", highest_mark, "| Lowest:", lowest_mark)

above_80 = [subj for subj, mark in student.items() if mark > 80]
if above_80:
    print("No of subjects student scored above 80 is", len(above_80), above_80)
else:
    print("failed")

Student = {
    'Maths': 34,
    'Physics': 56,
    'Chemistry': 92,
    'Computer science': 78,
    'English': 79
}

for subject, mark in Student.items():
    print(f"{subject}: {mark}")    

print(student_name)
print(student_id)
print(age)
print("Total:", total)
print("Average:", avg)

