class Students:
    def __init__(self, name, age, phone, form, subjects, gender):
        self.name = name
        self.age = age
        self.phone = phone
        self.form = form
        self.subjects = subjects
        self.gender = gender
        self.enrolled = True
        student_list.append(self)


    def display_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nPhone number: {self.phone}"
              f"\nForm class: {self.form}\nSubjects: {self.subjects}\nGender: "
              f"{self.gender}\nEnrolled: {self.enrolled}")

    def display_name(self):
        print(f"Name: {self.name}")


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        teacher_list.append(self)

    def display_info(self):
        print(f"Teacher Name: {self.name}\nSubject: {self.subject}")


def integer_checker(question):
    error = "\nSorry, you must enter an integer\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


def get_classes():
    class_list = []
    for teacher in teacher_list:
        class_list.append(teacher.subject)
    return class_list


def get_form_classes():
    form_classes = []
    for teacher in teacher_list:
        form_classes.append(teacher.name.upper())
    return form_classes


def get_subjects(subject_options):
    subjects = []
    print(f"Available subjects are: {", ".join(subject_options)}")
    while True:
        subject = input("Enter a subject (or type 'X' to finish): ")
        subject_no_spaces = subject.strip()
        if subject_no_spaces.lower() == "x":
            break
        elif subject_no_spaces.upper() in subject_options:
            subjects.append(subject_no_spaces.upper())
        else:
            print("Please enter a subject in the list")
    return ", ".join(subjects)


def get_gender():
    while True:
        gender = input("Enter the students gender: ").title()
        if gender == "Female" or gender == "Male":
            return gender
        print("Please enter 'Male' or 'Female'")


def get_form_class(form_class_options):
    print(f"Form classes are:", ", ".join(form_class_options))
    while True:
        form_class = input("Enter the students form class: ")
        form_no_spaces = form_class.strip()
        if form_no_spaces.upper() in form_class_options:
            return form_no_spaces.upper()
        else:
            print("Please choose one of the form classes")


def add_students(subjects_list, form_classes):
    name = input("Enter the students name: ").title()
    age = integer_checker("Enter the students age: ")
    phone = input("Enter the students phone number: ")
    form = get_form_class(form_classes)
    subjects = get_subjects(subjects_list)
    gender = get_gender()
    Students(name, age, phone, form, subjects, gender)


def print_student_details():
    for student in student_list:
        student.display_info()


def print_teacher_details():
    for teacher in teacher_list:
        teacher.display_info()


def select_student_age():
    age_requirement = integer_checker("Please enter the minimum age to search "
                                      "for: ")
    count = 0
    for student in student_list:
        if student.age >= age_requirement:
            count += 1
            student.display_info()
    print(f"\nThere are {count} students at {age_requirement} or older")


def count_students(subject_options):
    print(f"Subjects available are:", ", ".join(subject_options))
    while True:
        class_to_search = input("What class are you looking for: ").upper()
        if class_to_search in subject_options:
            count = 0
            for student in student_list:
                subjects_list = student.subjects.split(", ")
                if class_to_search in subjects_list:
                    count += 1
            for teacher in teacher_list:
                if teacher.subject == class_to_search:
                    return count, teacher.name
        else:
            print("Please choose one of the classes")


def find_student():
    while True:
        student_to_find = input("Enter the student you want to finds name: "
                                "").title()
        found = False
        for student in student_list:
            if student.name == student_to_find:
                student.display_info()
                found = True
                break
        if found:
            break
        else:
            print("Student not found in system")
            break


def print_gender():
    while True:
        chosen_gender = (input("Enter the gender of students to print: ")
                         .title())
        if chosen_gender == "Male":
            choice = "Male"
            break
        elif chosen_gender == "Female":
            choice = "Female"
            break
        else:
            print("Please choose 'Male' or 'Female'")
    count = 0
    for students in student_list:
        if students.gender == choice:
            count += 1
            students.display_name()
    print(f"\nThere are {count} {choice} students")


def generate_students():
    # Imports csv module so python can work with this file
    import csv
    # With ensures file is closed when function stops, newline='' prevents
    # extra blank rows from python so csv module can do all the work, csvfile
    # is now the variable of the file
    with open('random_students.csv', newline='') as csvfile:
        # csv.reader creates a reader object to read the file. Delimiter=|
        # tells the module that the values are separated by the | not a comma
        filereader = csv.reader(csvfile, delimiter='|')
        # line is a list of strings. Each line is a new student
        for line in filereader:
            # Checks if student is male
            if line[5] == "True":
                gender = "Male"
            else:
                gender = "Female"
            # Adds student values to class object
            Students(line[0], int(line[1]), line[2], line[3], line[4], gender)


def menu(class_options, form_classes):
    new_action = True
    while new_action:

        print()
        print("1. Add a student to the system")
        print("2. Print all student details")
        print("3. Print details of all students above a particular age")
        print("4. Count the number of students in a particular subject")
        print("5. Print details of a particular student")
        print("6. Print all teacher details")
        print("7. Print all students of specific gender")
        print("8. Exit")

        choice = input("\nWhat would you like to do? - Enter a number: ")
        if choice == "1":
            add_students(class_options, form_classes)

        elif choice == "2":
            print_student_details()

        elif choice == "3":
            select_student_age()

        elif choice == "4":
            counted_students, teacher = count_students(class_options)
            if counted_students == 0:
                print("\nThere are no students in this class")
            else:
                print(f"\nThere are {counted_students} students in {teacher}'s"
                      f" class")

        elif choice == "5":
            find_student()

        elif choice == "6":
            print_teacher_details()

        elif choice == "7":
            print_gender()

        elif choice == "8":
            print("Goodbye")
            new_action = False

        else:
            print("\nPlease choose one of the available options\n")


# Main routine
student_list = []
teacher_list = []

generate_students()

Teacher("Baker", "GRA")
Teacher("Barker", "MAT")
Teacher("Graham", "BIO")
Teacher("Morgan", "DTC")
Teacher("Bell", "PHY")
Teacher("Nimmo", "ART")
Teacher("McNicol", "ENG")

classes = get_classes()
available_form_classes = get_form_classes()

menu(classes, available_form_classes)
