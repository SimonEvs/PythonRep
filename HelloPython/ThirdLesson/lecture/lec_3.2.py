# list=[]

# for i in range(1,101):
#     if(i%2==0):
#         list.append(i)

# print(list)



# list=[i for i in range(1,101) if i%2==0]
# print(list)


# def f(x):
#     return x**3

# list=[f(i) for i in range(1,21) if i%2==0]
# print(list)

#Добавим кортежи)


# def f(x):
#     return x**3

# list=[(i,f(i)) for i in range(1,21) if i%2==0]
# print(list)

#Задача:
def f(x):
    return x**2
my_list=[1,2,3,5,8,15,23,38]
list=[(i,f(i)) for i in my_list if i%2==0]

print(list)

