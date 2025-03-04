class Dog:
    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour

    def print_details(self):
        return f"{self.name} is a {self.colour} dog aged {self.age}"

    def change_age(self, age):
        self.age = age

