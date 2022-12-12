class Phone: # base class / parent class
    def __init__(self,brand,model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)
    
    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def   make_a_call(self,number):
        return f"calling {number}...."


class Smartphone:
    def __init__(self, brand,model_name, price,ram, internal_memory, rear_camera):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def make_a_call(self,number):
        return f"calling {number}...."


phone = Phone('nokia', '1100', 1000)        
smartphone= Smartphone('oneplus' , 'S' , 30000, '6 GB', '64 GB', '20 MP')
print(phone.full_name())
print(smartphone.full_name())