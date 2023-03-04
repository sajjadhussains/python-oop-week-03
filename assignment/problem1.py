# . Create a function exp(a, n) that returns the exponential result ( an ). Read user input a and n in a single line from the keyboard.

# Example input:
# >> enter numbers: 2 3

# Example Output:
# >> result is: 8


def exp(a,n):
    return a**n

a,b=input("enter numbers: ").split()
num1=int(a)
num2=int(b)
result = exp(num1,num2)
print(result)


