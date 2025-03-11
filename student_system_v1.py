class Students:
    def __init__(self, name, age, phone, form, subjects):
        self.name = name
        self.age = age
        self.phone = phone
        self.form = form
        self.subjects = subjects
        self.gender = True
        self.enrolled = True
        

    def display_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nPhone number: {self.phone}"
              f"\nForm class: {self.form}\nSubjects: {self.subjects}\nGender: "
              f"{self.gender}\nEnrolled: {self.enrolled}")


s1 = Students("Raf", "69", "037333773", "13NIG", "Math")
Students.display_info(s1)
s1.display_info()