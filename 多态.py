# 每个子类都使用同一个名字的属性，但是这些属性会在各个子类中有所不同，然后用for loop来遍历这些属性 
# 这样看来，我们虽然只调用了一次，但是实际上调用了每个子类的属性
class Animal:
    def __init__(self, Animal):
        print(Animal, 'is an animal.')

class Mammal (Animal):
    def __init__(self, mammalName) :
        print(mammalName, 'is a warm-blooded animal')
        super().__init__(mammalName)

class NonWingedMammal (Mammal):
    def __init__(self, NonWingedMammal):
        print(NonWingedMammal, "can't fly.")
        super().__init__(NonWingedMammal)

class NonMarineMammal (Mammal):
    def __init__(self, NonMarineMammal):
        print(NonMarineMammal, "can't swim.")
        super().__init__(NonMarineMammal)

class Dog(NonMarineMammal, NonWingedMammal):
    def __init__(self):
        print('Dog has 4 legs.')
        super().__init__('Dog')
        
d = Dog()