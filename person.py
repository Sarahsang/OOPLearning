class Person():
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def show(self):
        print(self.name, self.age)
    def speak(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old"
    
def HeightCheck(aHeight):
    for student in students:
        if student.height > aHeight:
            print(f"{student.name} is taller than {aHeight}")
        else:
            print(f"{student.name} is shorter than {aHeight}")
    
person1 = Person("John", 36, 1.75)
person2 = Person("Mary", 25, 1.65)
person3 = Person("Bob", 27, 1.80)
person4 = Person("Jane", 21, 1.70)
person5 = Person("Peter", 29, 1.68)

students = []
students.append(person1)
students.append(person2)
students.append(person3)
students.append(person4)    
students.append(person5)

#pop移除并返回被移除的元素
# PersonPop = students.pop(1)
# print(PersonPop.speak())

#check height
HeightCheck(1.70)

print(students)

for student in students:
    student.show()
