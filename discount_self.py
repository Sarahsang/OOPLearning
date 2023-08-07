class laptop:
    discount = 10
    def __init__(self,brand_name,price):
        # instance variable
        self.brand_name = brand_name
        self.price = price
        
    def apply_discount(self):
        off_price = (self.price/100) * self.discount
        final_amount = self.price - off_price
        return final_amount
    
m550 = laptop('HP',50000)
print(m550.apply_discount())
# 格式化 formatting
print("{} {} {}".format(m550.brand_name,m550.price,m550.apply_discount()))