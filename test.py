import unittest
import Student as s
import Classroom as c


class ClassTest(unittest.TestCase):
    def setUp(self):
        print(f"Test {self._testMethodName} being executed...")
        self.students = []

        try:
            self.students.append(s.Student("Luiza", "Fonseca", 10))
            self.students.append(s.Student("Mariana", "Ferreira", 8))
            self.students.append(s.Student("Chico", "Assis", 6))
            self.students.append(s.Student("Amy", "Fonseca", 7))
            self.students.append(s.Student("Amanda", "Santos", -1))
        except:
            pass
            
        self.classroomObject = c.Classroom()
        self.classroomObject.add_students(self.students)

    def tearDown(self):
        print(f"Test {self._testMethodName} finished.")

    def testHighestGrade(self):
            self.assertEqual(
                10, self.classroom.highest_grade.grade, "Error finding the highest grade"
            )
    
    def testLowestGrade(self):
            self.assertEqual(
                6, self.classroom.lowest_grade.grade, "Error finding the lowest grade"
            )

    def testGradeRange(self):
        print("Testing if the grade range is correct.")
        for student in self.classroom.students:
            self.assertGreaterEqual(
                student.grade, 0, f"Grade less than 0 found for {student.first_name}."
            )
            self.assertLessEqual(
                student.grade, 10, f"Grade greater than 10 found for {student.first_name}."
            )


if __name__ == "__main__":
    unittest.main()
