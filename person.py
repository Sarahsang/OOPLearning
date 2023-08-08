class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)
    def speak(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old"
    
person1 = Person("John", 36)
person2 = Person("Mary", 25)
person3 = Person("Bob", 27)
person4 = Person("Jane", 21)
person5 = Person("Peter", 29)

students = []
students.append(person1)
students.append(person2)
students.append(person3)
students.append(person4)    
students.append(person5)

#pop移除并返回被移除的元素
PersonPop = students.pop(1)
print(PersonPop.speak())