class Phone:
    # static attribute
    manufectured:'America'
    def __init__(self,price,color,brand):
        self.price = price
        self.color = color
        self.brand = brand
    def send_msg(self):
        print('all are quality products')

my_phone = Phone(30000,'blue','real me')
her_phone = Phone(100000,'black','iphone')

print(f'This is my phone: {my_phone.price},{my_phone.color},{my_phone.brand}')
print(her_phone.price,her_phone.color,her_phone.brand,her_phone.send_msg())