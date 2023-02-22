class Shop:
    cart=[]
    def __init__(self,buyer):
        self.buyer=buyer
    def add_to_cart(self,item):
        self.cart.append(item)

shop1=Shop('hatem')
shop1.add_to_cart('tshirt')
shop1.add_to_cart('3 quarter pant')
print(shop1.cart)