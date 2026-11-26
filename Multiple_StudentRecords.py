students = [
    {
        "name": "Arjun","id": "99999","marks": {"Maths": 78, "Physics": 89, "Chemistry": 95, "Computer science": 56, "English": 70},
        "attendance": "Eligible",
    },
    {
        "name": "Akash","id": "98764","marks": {"Maths": 85, "Physics": 82, "Chemistry": 79, "Computer science": 91, "English": 88},
        "attendance": "Eligible",
        "id": "S102",
    },
    {
        "name": "Gautham", "id": "98760","marks": {"Maths": 45, "Physics": 38, "Chemistry": 62, "Computer science": 54, "English": 49},
        "attendance": "Eligible",
    },
    {
        "name": "Abhinav", "id": "78096", "marks": {"Maths": 92, "Physics": 90, "Chemistry": 88, "Computer science": 94, "English": 86},
        "attendance": "Shortage",
    },
    {
        "name": "Karthik",  "id": "67980","marks": {"Maths": 66, "Physics": 72, "Chemistry": 68, "Computer science": 74, "English": 61},
        "attendance": "Eligible",
    },
]

pass_mark = 45
passed_students = []
failed_students = []

for student in students:
    marks_list = list(student["marks"].values())
    has_attendance = student["attendance"] == "Eligible"
    passed_all_subjects = min(marks_list) >= pass_mark

    if has_attendance and passed_all_subjects:
        passed_students.append(student["name"])
    else:
        failed_students.append(student["name"])

top_student = max(
    students,
    key=lambda s: sum(s["marks"].values()) / len(s["marks"])
)
top_avg = sum(top_student["marks"].values()) / len(top_student["marks"])

print("Passed students:", passed_students)
print("Failed students:", failed_students)
print("No of students passed:", len(passed_students))
print(f"Highest average: {top_student['name']} ({top_avg:.2f})")