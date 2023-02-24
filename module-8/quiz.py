class Sales:
    def __init__(self, id):
        self.id = id
        id = 100

val = Sales(123)
# print (val.id) ---output will be 123 When the object val of the Sales class is created with the argument 123, the __init__ method is called with self referring to the object val and id set to 123. Thus, self.id is set to 123.

# The line id = 100 inside the __init__ method creates a local variable id with the value 100, but it does not affect the value of self.id which is already set to 123.
class People():
    def __init__(self, name):
      self.name = name

    def namePrint(self):
      print(self.name)

person1 = People("Emma")
person2 = People("Watson")
# person1.namePrint()
class Person:
    def __init__(self, id):
        self.id = id

sam = Person(100)
sam.__dict__['age'] = 49

print (sam.__dict__)