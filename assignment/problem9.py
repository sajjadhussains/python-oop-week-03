class Calculate:
    def __init__(self,X,n):
        self.x=X
        self.n=n
    def sum(self):
        return self.x+self.n
    def pow(self):
        return self.x**self.n
    
new_obj = Calculate(2,3)
result1 = new_obj.sum()
result2 = new_obj.pow()
print(result1,result2)