student_marks = [78, 89, 95, 56, 70]
for mark in student_marks:
    if mark < 40:
        grade = "Failed"
    elif mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 70:
        grade = "C"
    elif mark >= 60:
        grade = "D"
    elif mark >= 50:
        grade = "E"
    else:
        grade = "Failed"

    print(f"Mark: {mark} -> Grade: {grade}")   

attendance = 80
min_attendance = 75

if attendance < min_attendance and min_attendance > 75:
    print("Attendance shortage") 
    print('Failed')
else:
    print('Full Attendence')   
    print('Passed')

if attendance > min_attendance and min_attendance > 75:
    print('Attendance shortage')
    print('Failed')
else:
   print('Full Attendence')   
   print('Passed')
