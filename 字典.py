class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 500:
            return 'Pass'
        else:
            return 'Fail'


s1 = Student("Miao", 600)
s2 = Student("Sang", 400)
s3 = Student("emma", 200)
s4 = Student("Marky", 700)
s5 = Student("rebort", 300)
s6 = Student("ema", 600)

student_objects = [s1, s2, s3, s4, s5, s6]
passStudents = []
failStudents = []
students_result = {}
for x in student_objects:
    if x.result() == 'Pass':
        passStudents.append(x.name)
        students_result['Pass Students']=passStudents
    else:
        failStudents.append(x.name)
        students_result['Fail Students']=failStudents

print(students_result)
