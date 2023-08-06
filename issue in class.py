class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name =  model_name
        self.price =  max(price,0)
#         if price > 0:
#             self.price = price
#         else:
#             self.price = 0
        self.completeSpecification = f"{self.brand} {self.model_name} and price is {self.price}"

    # @property 
    # def completeSpecification(self):
    #     return f"{self.brand} {self.model_name} and price is {self.price}" 
    @staticmethod
    def make_a_call(phone_num):
        print(f"calling {phone_num}...")
    
    def full_name(self):
        return f"{self.brand} {self.model_name}"