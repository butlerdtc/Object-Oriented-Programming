# Base class/Superclass
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what to say")


# Subclass
class Cat(Pet):
    # This overrides the method in the parent class
    def speak(self):
        print("Meow")


# Subclass
class Dog(Pet):
    def speak(self):
        print("Bark")


# Subclass
class Snake(Pet):
    # Initializes the objects
    def __init__(self, name, age, colour):
        # Calls the superclass to initialize the attributes from it.
        super().__init__(name, age)
        # Sets the unique attribute
        self.colour = colour

    # Overrides function from superclass
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
