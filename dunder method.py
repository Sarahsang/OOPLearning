class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def str(self):
        return f"{self.name}, {self.age} years old"
    
a = Person("John", 36)
print(a)
