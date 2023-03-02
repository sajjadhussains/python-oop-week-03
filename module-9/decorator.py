
import math
import time


def timer(func):
    def inner(*args,**kwargs):
        print(f'Time start ')
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print(f'Time end with {end-start}')
    return inner
@timer
def get_factorial(n=30):
    result = math.factorial(n)
    print(f'factorial of {n} is:{result}')


get_factorial()