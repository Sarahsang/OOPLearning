class laptop:
    def __init__(self,brand_name,price):
        self.brand_name = brand_name
        self.price = price
        self.laptop_name = brand_name + ' ' + price
        
m545 = laptop('HP','50000')

print(m545.__dict__.keys())
