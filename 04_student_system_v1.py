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


def integer_checker(question):
    error = "\nSorry, you must enter an integer\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


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


def select_student_age():
    age_requirement = integer_checker("Please enter the minimum age to search "
                                      "for: ")
    count = 0
    for student in student_list:
        if student.age >= age_requirement:
            count += 1
            student.display_info()
    print(f"There are {count} students at {age_requirement} or older")


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
            return count
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


# Main routine
classes = ["ART", "ENG", "MAT", "GRA", "DTC", "PHY", "BIO"]
available_form_classes = ["BAKER", "MORGAN", "MCNICOL", "GRAHAM", "BELL",
                          "NIMMO", "BARKER"]
student_list = []
generate_students()

new_action = True
while new_action:
    print("1. Add a student to the system")
    print("2. Print all student details")
    print("3. Print details of all students above a particular age")
    print("4. Count the number of students in a particular subject")
    print("5. Print details of a particular student")
    print("6. Exit")

    choice = input("\nWhat would you like to do? - Enter a number: ")
    if choice == "1":
        add_students(classes, available_form_classes)
    elif choice == "2":
        print_student_details()
    elif choice == "3":
        select_student_age()
    elif choice == "4":
        counted_students = count_students(classes)
        print(counted_students)
    elif choice == "5":
        find_student()
    elif choice == "6":
        print("Goodbye")
        new_action = False
    else:
        print("\nPlease choose one of the available options\n")
