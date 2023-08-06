class laptop:
    def __init__(self,brand_name,price):
        self.brand_name = brand_name
        self.price = price
        self.laptop_name = brand_name + ' ' + price

#creating object        
m545 = laptop('HP','50000')

print(m545.__dict__.keys())

m4800 = laptop('Dell','60000')

#adding new attribute to m4800
m4800.bluetooth = 'yes'

print(m4800.__dict__)