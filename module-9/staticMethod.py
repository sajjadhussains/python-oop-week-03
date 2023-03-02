class Shopping:
    def __init__(self,customer):
        self.customer = customer
        self.items=[]
        self.total = 0
    @staticmethod
    def multiply(x,y):
        return x*y

    def add_to_total(self,amount):
        self.total+=amount

    def add_to_cart(self,item,price,quantity):
        item_total=price*quantity
        self.add_to_total(item_total)
        self.items.append(item)

result_1 = Shopping.multiply(45,5)
print(result_1)

shopping = Shopping('manju mia')
shopping.add_to_total(450)
shopping.add_to_total(450)
print(shopping.total)