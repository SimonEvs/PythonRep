from tkinter import Y


# def sum(x, y):             #То, что написано здесь.
#     return x+y

sum=lambda x,y:x+y         #Это то же самое, что и здесь.

def mylt(x, y):
    return x*y


def calc(op, a, b):
    print(op(a,b))
    # return op(a,b)


calc(sum,10,2)

#А можем сделать так 
calc(lambda x,y:x+y,4,5)        

