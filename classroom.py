class Classroom:
    def __init__(self):
        self.classroom = []
        self.lowest_grade = None
        self.highest_grade = None

    def add_students(self, students):
        for student in students:
            self.classroom.append(student)
            if self.lowest_grade is None or self.lowest_grade.grade > student.grade:
                self.lowest_grade = student
            if self.highest_grade is None or self.highest_grade.grade < student.grade:
                self.highest_grade = student

    def show_students(self):
        print("Number of students:", len(self.students))
        for student in self.classroom:
            print(student.show_student())
