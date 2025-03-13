class Students:
    student_list = []

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
    age = input("Enter the students age: ")
    phone = input("Enter the phone number: ")
    form = input("Enter the students form class: ").upper()
    subjects = get_subjects()
    gender = get_gender()
    Students(name, age, phone, form, subjects, gender)


# Main routine
add_students()
