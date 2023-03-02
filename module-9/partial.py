
from functools import partial


def get_number(a,b,c,d):
    return a*100+b*3+c*5+d*3

number = get_number(4,5,6,7)
fourth_only = partial(get_number,b=0,c=0,d=0)
number2=fourth_only(4)
print(number2)
