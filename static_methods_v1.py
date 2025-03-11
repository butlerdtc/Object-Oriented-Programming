class AllStaff:
    number_of_staff = 0
    RETIREMENT_AGE = 65

    def __init__(self, name, age, id, birthdate, job):
        self.name = name
        self.age = age
        self.id = id
        self.birthdate = birthdate
        self.job = job

        AllStaff.calc_number_of_staff()


    def show(self):
        print(f"Added {self.id} is {self.name} aged {self.age} being born "
              f"{self.birthdate} employed as {self.job}")

    @classmethod
    def calc_number_of_staff(cls):
        cls.number_of_staff += 1

    @classmethod
    def total_staff(cls):
        return cls.number_of_staff


class Management(AllStaff):
    def __init__(self, name, age, id, birthdate, job, car):
        super().__init__(name, age, id, birthdate, job)
        self.car = car
    def show(self):
        print(f"Added {self.id} is {self.name} aged {self.age} being born "
              f"{self.birthdate} employed as {self.job} driving a {self.car}")

class Clerical(AllStaff):
    def __init__(self, name, age, id, birthdate, job, typing_speed):
        super().__init__(name, age, id, birthdate, job)
        self.typing_speed = typing_speed
    def show(self):
        print(f"Added {self.id} is {self.name} aged {self.age} being born "
              f"{self.birthdate} employed as {self.job} with a typing speed of"
              f" {self.typing_speed}")

class Factory(AllStaff):
    pass


a = Management("Jenny", 22, "ID007", "20/10/2000",
               "Managing Director", "Jaguar")
print(f"Total number of staff is now {AllStaff.total_staff()}")
a.show()
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