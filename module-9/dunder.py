class Person():
    def __init__(self,name,age,money) -> None:
        self.name=name
        self.age=age
        self.money=money
    def __add__(self,other):
        return self.money+other.money

alim = Person('alim',19,20)
dalim = Person('dalim',20,10)
kalim = Person('kalim',20,20)
print(alim+dalim)