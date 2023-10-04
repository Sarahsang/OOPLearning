# 类的继承 子类继承父类的属性和方法
# 1.单继承
# class ParentClass(object):
#     def __init__(self):
#         self.name = 'ParentClass'
#         print('ParentClass')
#     def parentFunc(self):
#         print('parentFunc')

# class ChildClass(ParentClass):
#     def __init__(self):
#         print('ChildClass')
#     def childFunc(self):
#         print('childFunc')

# c = ChildClass()
# c.childFunc()
# c.parentFunc()
# print(c.name)

class Mammal:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.num_eyes = 2
    
    def breathe(self):
        print(self.name + ' is breathing')
        
    def poop(self):
        print(self.name + ' is pooping')
 
# 子类直接继承父类的构造函数       
# class Human(Mammal):
#     def read(self):
#         print(self.name + ' is reading')
        
# class Cat(Mammal):
#     def meow(self):
#         print(self.name + ' is meowing')
        
#     def poop(self): #如果子类有自己的方法，会覆盖父类的方法 第30行
#         print(self.name + ' is pooping in a box')

#如果想在子类里面添加新的构造函数同时还要继承父类的构造函数，可以用super()函数
class Human(Mammal):
    def __init__(self, name, sex):
        super().__init__(name, sex)
        self.has_tail = False    
    
    def read(self):
        print(self.name + ' is reading')
# 继承父类构造函数的同时还可以添加新的属性
class Human(Mammal):
    def __init__(self, name, sex, degree):
        super().__init__(name, sex)
        self.degree = degree #添加新的属性
    
    def read(self):
        print(self.name + ' is reading')
                
class Cat(Mammal):
    def __init__(self, name, sex):
        super().__init__(name, sex)
        self.has_tail = True 
    
    def meow(self):
        print(self.name + ' is meowing')
        
cat1=Cat('maomao', 'girl') #实例化
print(cat1.num_eyes)  # 输出 num_eyes 的值
print(cat1.has_tail)  # 输出 has_tail 的值
       
# 2.多继承
# class ParentClass1(object):
#     def __init__(self):
#         self.name1 = 'ParentClass1'
#         print('ParentClass1')
#     def parentFunc1(self):
#         print('parentFunc1')
#
# class ParentClass2(object):
#     def __init__(self):
#         self.name2 = 'ParentClass2'
#         print('ParentClass2')
#     def parentFunc2(self):
#         print('parentFunc2')
#
# class ChildClass(ParentClass1,ParentClass2):
#     def __init__(self):
#         print('ChildClass')
#     def childFunc(self):
#         print('childFunc')
#
# c = ChildClass()
# c.childFunc()
# c.parentFunc1()
# c.parentFunc2()
# print(c.name1)
# print(c.name2)

# 3.多重继承
# class ParentClass1(object):
#     def __init__(self):
#         self.name1 = 'ParentClass1'
#         print('ParentClass1')
#     def parentFunc1(self):
#         print('parentFunc1')
#
# class ParentClass2(object):
#     def __init__(self):
#         self.name2 = 'ParentClass2'
#         print('ParentClass2')
#     def parentFunc2(self):
#         print('parentFunc2')
#
# class ChildClass(ParentClass1,ParentClass2):
#     def __init__(self):
#         print('ChildClass')
#     def childFunc(self):
#         print('childFunc')
#
# c = ChildClass()
# c.childFunc()
# c.parentFunc1()
# c.parentFunc2()
# print(c.name1)
# print(c.name2)

# 4.方法重写
# class ParentClass(object):
#     def __init__(self):
#         self.name = 'ParentClass'
#         print('ParentClass')
#     def parentFunc(self):
#         print('parentFunc')
#
# class ChildClass(ParentClass):
#     def __init__(self):
#         print('ChildClass')
#     def childFunc(self):
#         print('childFunc')
#     def parentFunc(self):
#         print('childFunc')
#
# c = ChildClass()
# c.childFunc()
# c.parentFunc()
# print(c.name)

# 5.调用未绑定的父类方法
# class ParentClass(object):
#     def __init__(self):
#         self.name = 'ParentClass'
#         print('ParentClass')
#     def parentFunc(self):
#         print('parentFunc')
#
# class ChildClass(ParentClass):
#     def __init__(self):
#         print('ChildClass')
#     def childFunc(self):
#         print('childFunc')
#     def parentFunc(self):
#         print('childFunc')
#         ParentClass.parentFunc(self)
#
# c = ChildClass()
# c.childFunc()
# c.parentFunc()
# print(c.name)
