# parameter can pass in another function in python
def do_something(work):
    print('outside function call want to see')
    work()
    print('yaa!looks good')

def working():
    print('look,i can do from outside')

# do_something(working)

# A function can call within a function and also can be call from that function
# A function can return also from a function