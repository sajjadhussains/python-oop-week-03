class Person:
    def __init__(self,name,age,salary) -> None:
        self.name=name
        self.age=age
        self.salary = salary
    def __eq__(self, other) -> bool:
        return self.age == other.age

alim=Person('alim',3,1)
dalim = Person('dalim',3,2)
print(alim==dalim)

# dunder method in python