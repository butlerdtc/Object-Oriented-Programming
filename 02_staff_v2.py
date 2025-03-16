# Superclass
class AllStaff:
    # Class attributes
    number_of_staff = 0
    # (Class constant)
    RETIREMENT_AGE = 65

    # Creates class objects
    def __init__(self, name, age, id, birthdate, job):
        self.name = name
        self.age = age
        self.id = id
        self.birthdate = birthdate
        self.job = job

        # Uses static method to add 1 to staff list as object made
        AllStaff.calc_number_of_staff()

    # Method to print details out
    def show(self):
        print(f"Added {self.id} is {self.name} aged {self.age} being born "
              f"{self.birthdate} employed as {self.job}")

    # Static methods to interact with number of staff
    @classmethod
    def calc_number_of_staff(cls):
        cls.number_of_staff += 1

    @classmethod
    def total_staff(cls):
        return cls.number_of_staff


# Subclass
class Management(AllStaff):
    def __init__(self, name, age, id, birthdate, job, car):
        # Uses superclass to create object attributes
        super().__init__(name, age, id, birthdate, job)
        # Adds unique attribute
        self.car = car
    # Overrides show method in superclass
    def show(self):
        print(f"Added {self.id} is {self.name} aged {self.age} being born "
              f"{self.birthdate} employed as {self.job} driving a {self.car}")


# Subclass
class Clerical(AllStaff):
    # Creates object
    def __init__(self, name, age, id, birthdate, job, typing_speed):
        # Uses superclass to create attributes
        super().__init__(name, age, id, birthdate, job)
        # Adds unique attribute
        self.typing_speed = typing_speed

    # Overrides show method in superclass
    def show(self):
        print(f"Added {self.id} is {self.name} aged {self.age} being born "
              f"{self.birthdate} employed as {self.job} with a typing speed of"
              f" {self.typing_speed}")

# Subclass
class Factory(AllStaff):
    # No unique attributes so it inherits it all from superclass (pass is
    # placeholder)
    pass


# Main routine
# This creates an object with variable name
a = Management("Jenny", 22, "ID007", "20/10/2000",
               "Managing Director", "Jaguar")
# Calls static method to show total number of staff
print(f"Total number of staff is now {AllStaff.total_staff()}")
# Runs show method
a.show()
# Calls class constant to calculate age until retirement
print(f"NOTE: Only {AllStaff.RETIREMENT_AGE - a.age} years until {a.name} "
      f"retires")
print()

b = Clerical("Tim", 17, "ID119", "01/01/2005",
             "Secretary", 123)
print(f"Total number of staff is now {AllStaff.total_staff()}")
b.show()
print(f"NOTE: Only {AllStaff.RETIREMENT_AGE - b.age} years until {b.name} "
      f"retires")
print()

c = Factory("Jake", 16, "ID125", "17/08/2006",
            "Labourer")
print(f"Total number of staff is now {AllStaff.total_staff()}")
c.show()
print(f"NOTE: Only {AllStaff.RETIREMENT_AGE - c.age} years until {c.name} "
      f"retires")
print()
