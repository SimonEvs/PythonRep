# def f(x):
#     return x**2

# g =f 

# print(type(f))
# print(f(4))
# print(g(4))

def calc1(x):
    return x+10

# print(calc1(10))


def calc2(x):
    return x*10

# print(calc2(10))


def math(op,x):
    print(op(x))

math(calc2,10)
math(calc1,10)