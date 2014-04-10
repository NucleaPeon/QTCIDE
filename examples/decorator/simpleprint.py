'''
Using the '@' sign to decorate a method is essentially saying that
"I want to use this method as the callable parameter, instead of using
the following:
    example = deco(init)
    example()
    
you use:
    @deco
    def example():
        pass
    
    # example() adds itself to deco --> deco(example) when called
'''


'''
Decorated version using @
'''

def wrapper(callable_func):
    def fail(x, y, *args, **kwargs):
        print("Fail")
        return -1
    
    def add(x, y, *args, **kwargs):
        print("add")
        a = x + y
        for z in args:
            a = a + z
        return a
    # Call based on callable's name
    if str(callable_func.__name__) == "add":
        return add
    return fail

@wrapper
def add(a, b): # a and b are not required?
    return a + b

@wrapper
def notadd(a, b):
    return a + b

add(1, 2)
notadd(1, 2)
add(4, 4)
add(1, 10)
add(1, 2, 3, 4, 5, 6, 7, 8, 9, 0) # 45
