class Student:
    def __init__(self,Student_name,Student_id,marks,attendence_status):
        self.Student_name =Student_name
        self.Student_id = Student_id
        self.marks = marks
        self.attendence_status = attendence_status

    def calculate_total():

        @property
        def marks(self):
            return self.marks

        @marks.setter
        def marks(self,new_marks):
            self.new_marks =new_marks

    def calculate_total(self):
        return sum(self.__marks.values())

    def calculate_average(self):
        return self.calculate_total() / len(self.marks)
    
    def passed_all_subjects(self):
        return min(self.marks.values()) >= self.pass_mark
    
    def calculate_grade(self):
        if not self.passed_all_subjects():
            return "Failed"

        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        elif avg >= 50:
            return "E"
        else:
            return "Failed"

    def display_details(self):
        print(f"Name: {self.student_name} | ID: {self.student_id} | Attendance: {self.attendance_status}")
        for subject, mark in self.__marks.items():
            print(f"  {subject}: {mark}")
        print(f"Total: {self.calculate_total()} | Average: {self.calculate_average():.2f} | Grade: {self.calculate_grade()}")
        print("-" * 45)    


student_1 =Student('Arjun','23456',89,'Eligible')
        