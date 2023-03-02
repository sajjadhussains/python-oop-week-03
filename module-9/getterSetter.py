class User:
    def __init__(self,f_name,l_name):
        self.first = f_name
        self.last = l_name
        self.email = f'{self.first}.{self.last}@gmail.com'
    @property
    def full_name(self):
        return f'{self.first} {self.last}'
    @full_name.setter
    def full_name(self,value):
        first,last = value.split(' ')
        self.first = first
        self.last = last
        self.email=f'{self.first}.{self.last}@gmail.com'
        # self.first = value.split(' ')[0]
        # self.last = value.split(' ')[1]
    @property
    def get_email(self):
        return self.email
    
mark = User('mark','zuku')
print(mark.first)
print(mark.last)
print(mark.email)
print(mark.get_email)
# mark.first ='Elun'
# print(mark.first)
print(mark.email)
mark.full_name="Tom hanks"
print(mark.first)
print(mark.last)
print(mark.full_name)
print(mark.email)
        