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


def get_subjects():
    subjects = []
    while True:
        subject = input("Enter a subject (or type 'X' to finish): ")
        if subject.lower() == "x":
            break
        subjects.append(subject)
    return subjects


def get_gender():
    while True:
        gender = input("Enter the students gender: ").title()
        if gender == "Female" or gender == "Male":
            return gender
        print("Please enter 'Male' or 'Female'")


def add_students():
    name = input("Enter the students name: ").title()
    age = integer_checker("Enter the students age: ")
    phone = input("Enter the phone number: ")
    form = input("Enter the students form class: ").upper()
    subjects = get_subjects()
    gender = get_gender()
    Students(name, age, phone, form, subjects, gender)


def print_student_details():
    for student in student_list:
        student.display_info()


def select_student_age():
    age_requirement = integer_checker("Please enter the minimum age to search "
                                      "for: ")
    for student in student_list:
        if student.age >= age_requirement:
            student.display_info()


def generate_students():
    # available form classes are: "BAKER", "MORGAN", "MCNICOL", "GRAHAM",
    # "BELL", "NIMMO", "BARKER"
    # available classes are: "ART", "ENG", "MAT", "GRA", "DTC", "PHY", "BIO"
    # Imports csv module so python can work with this file
    import csv
    # With ensures file is closed when function stops, newline='' prevents
    # extra blank rows from python so csv module can do all the work, csvfile
    # is now the variable of the file
    with open('random_students.csv', newline='') as csvfile:
        # csv.reader creates a reader object to read the file. Delimiter='|'
        # tells the module that the values are separated by the | not a comma
        filereader = csv.reader(csvfile, delimiter='|')
        # line is a list of strings. Each line is a new student
        for line in filereader:
            # Checks if student is male
            if line[5] == "True":
                is_male = True
            else:
                is_male = False
            # Adds student values to class object
            Students(line[0], int(line[1]), line[2], line[3], line[4], is_male)


# Main routine
student_list = []
generate_students()
# add_students()
# print_student_details()
# select_student_age()
student_list[0].display_info()
