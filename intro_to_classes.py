# A class acts like a blueprint to create objects
class Dog:
    # This creates (instantiation) objects with the parameters in the brackets
    def __init__(self, name, age, colour):
        # Self refers to this specific instance of the class (each object as
        # created)
        # self.name assigns the name parameter (2nd name) to the attribute of
        # the object (1st name)
        self.name = name
        self.age = age
        self.colour = colour

    # This is a method. A method can only interact with objects in its class
    def print_details(self):
        return f"{self.name} is a {self.colour} dog aged {self.age}"

    def change_age(self, age):
        self.age = age

# This creates a new object (dog1 and dog2)
dog1 = Dog("Spot", 7, "black")
dog2 = Dog("Jazz", 5, "white")

# This calls the method. Dog must be at the start as we are calling a method
# from a class and the object gets passed as an argument
print(Dog.print_details(dog1))
print(Dog.print_details(dog2))

dog1.change_age(17)
dog2.change_age(9)

print(Dog.print_details(dog1))
print(Dog.print_details(dog2))
