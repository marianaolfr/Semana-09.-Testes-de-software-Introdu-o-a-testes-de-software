class Student:
    def __init__(self, first_name, last_name, grade):
        if grade < 0 or grade > 10:
            raise ValueError(
                f"Invalid grade for student {first_name}. Grade must be between 0 and 10."
            )

        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade

    def show_student(self):
        return f"Student: {self.first_name} {self.last_name} - Grade: {self.grade}"
