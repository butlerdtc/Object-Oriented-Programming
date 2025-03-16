# See intro_to_classes
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
        # This creates a student list for each course
        self.students = []

    def add_student(self, student_):
        # Checks if the length of student list is less than the max
        if len(self.students) < self.max_students:
            # If true appends the student to the list and returns True
            self.students.append(student_)
            return True
        # If it can't fit the student it returns False
        return False

    def get_grade_average(self):
        total = 0
        # Iterates through each object (student) in the list
        for student_ in self.students:
            # This gets the students grade and adds it to the total
            total += student_.get_grade()
        # Returns the average grade
        return total / len(self.students)


# Main routine
# Creates objects in class and assigns them a variable name
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
