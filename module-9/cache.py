import time
from functools import cache


@cache
def fibo(n):
    if n<=1:
        return 1
    return fibo(n-1)+(n-2)

start = time.time()

for i in range(200):
    print(i,fibo(i))

end = time.time()
print('time took',(end-start)*1000)

# time took 11.963129043579102