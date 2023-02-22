class Laptop:
    def __init__(self,brand,age):
        self.brand=brand
        self.age = age
    def increase_age(self):
        self.age = self.age+1
my_laptop = Laptop('lenovo',1)
my_laptop.increase_age()
my_laptop.age = 17
print(my_laptop.brand,my_laptop.age)