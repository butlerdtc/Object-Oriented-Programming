class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what to say")


class Cat(Pet):
    def speak(self):
        print("Meow")


class Dog(Pet):
    def speak(self):
        print("Bark")


class Snake(Pet):
    def __init__(self, name, age, colour):
        super().__init__(name, age)
        self.colour = colour

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am "
              f"{self.colour}")


# Main routine
c = Cat("Tim", 7)
c.show()
c.speak()
print()

d = Dog("Jack", 10)
d.show()
d.speak()
print()

p = Pet("Liz", 5)
p.show()
p.speak()
print()

s = Snake("Hissy", 2, "Green")
s.show()
s.speak()