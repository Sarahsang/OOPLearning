class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id 
        
    def str (self):
        print(f"Employee name: {self.name}, id: {self.id}")
    
    def __str__ (self):
        return(f"Employee name: {self.name}, id: {self.id}")
    
    
    
    
class MyCollection:
    def __init__(self):
        self.items = []
    
    def add(self, item):
        self.items.append(item)


my_collection = MyCollection()
my_collection.add(1)
my_collection.add(2)
my_collection.add(3)

# 使用 len() 函数获取长度
print(my_collection.items) # 输出将会是 3
