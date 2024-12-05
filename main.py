import Student as s
import Classroom as c

students = []

for data in [
    ("Luiza", "Fonseca", 8),
    ("Mariana", "Ferreira", 10),
    ("Chico", "Assis", -1),
]:
    try:
        student = s.Student(*data)
        students.append(student)
    except:
        pass

classroomObject = c.Classroom()
classroomObject.add_students(alunos)

classroomObject.show_students()
print("*" * 30)
print("Student with lowest grade:", classroomObject.lowest_grade.show_students())
print("Student with highest grade:", classroomObject.highest_grade.show_students())
