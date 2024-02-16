class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll_course(self, course):
        """Method to enroll in a course."""
        self.courses.append(course)

    def display_info(self):
        """Method to display student information."""
        print(f"Student Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        if self.courses:
            print("Courses Enrolled:")
            for course in self.courses:
                print(f"- {course}")
        else:
            print("No courses enrolled yet.")

students = [
    Student("GIGO", "001"),
    Student("NIKA", "002"),
    Student("MISHA", "003")
]

students[0].enroll_course("Mathematics")
students[1].enroll_course("Physics")
students[2].enroll_course("History")

for student in students:
    student.display_info()
    print()
