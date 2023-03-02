class User:
    def __init__(self,name,password):
        self.name=name
        self.password = password

    def get_password(self,given_pass):
        if(self.password==given_pass):
            return True
        else:
            return False

user1=User('sajjad','shuvo')
result = user1.get_password('shuvo')
print(result)