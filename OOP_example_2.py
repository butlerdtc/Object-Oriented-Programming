class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student_):
        if len(self.students) < self.max_students:
            self.students.append(student_)
            return True
        return False

    def get_grade_average(self):
        total = 0
        for student_ in self.students:
            total += student_.get_grade()
        return total / len(self.students)


# Main routine
s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course1 = Course("Computer Science", 2)

course1.add_student(s1)
course1.add_student(s2)
print(course1.add_student(s3))

print(f"The average grade in {course1.name} is {course1.get_grade_average()}")

for student in course1.students:
    print(student.name)
