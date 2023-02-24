class Shopper:
    def __init__(self,name):
        self.name=name
        self.cart=[]
    def add_to_cart(self,item,price,quantity):
        self.cart.append({'item':item,'price':price,'quantity':quantity})
    def check_out(self,amount):
        price = 0
        for item in self.cart:
            print(item)
            price+=item['price']*item['quantity']
        if amount<price:
            return f'please give me more money:{price-amount}'
        elif amount>price:
            return f'Here is the item and extra money:{amount-price}'
        else:
            return 'Here are the items'
        
shopping = Shopper('SA brand')
shopping.add_to_cart('elitebook 840 g3',2400,1)
shopping.add_to_cart('elitebook 840 g4',3000,1)
shopping.add_to_cart('elitebook 840 g5',3500,1)

reply = shopping.check_out(8900)
print(reply)