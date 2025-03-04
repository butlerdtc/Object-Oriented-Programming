class AllStaff:
    def __init__(self, name, age, id, birthdate, job):
        self.name = name
        self.age = age
        self.id = id
        self.birthdate = birthdate
        self.job = job
    def show(self):
        print(f"{self.id} is {self.name} aged {self.age} being born "
              f"{self.birthdate} employed as {self.job}")

class Management(AllStaff):
    def __init__(self, name, age, id, birthdate, job, car):
        super().__init__(name, age, id, birthdate, job)
        self.car = car
    def show(self):
        print(f"{self.id} is {self.name} aged {self.age} being born "
              f"{self.birthdate} employed as {self.job} driving a {self.car}")

class Clerical(AllStaff):
    def __init__(self, name, age, id, birthdate, job, typing_speed):
        super().__init__(name, age, id, birthdate, job)
        self.typing_speed = typing_speed
    def show(self):
        print(f"{self.id} is {self.name} aged {self.age} being born "
              f"{self.birthdate} employed as {self.job} with a typing speed of"
              f" {self.typing_speed}")

class Factory(AllStaff):
    pass


a = Management("Jenny", 22, "ID007", "20/10/2000",
               "Managing Director", "Jaguar")
a.show()
print()

b = Clerical("Tim", 17, "ID119", "01/01/2005",
             "Secretary", 123)
b.show()
print()

c = Factory("Jake", 16, "ID125", "17/08/2006",
            "Labourer")
c.show()
