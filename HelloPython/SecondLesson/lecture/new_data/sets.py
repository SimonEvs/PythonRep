#Множества

# colors ={'red','green','blue'}
# print(type(colors))
# colors.add('red')
# print(colors)
# colors.add('gray')
# print(colors)
# colors.remove('red')
# print(colors)
# colors.discard('red')
# print(colors)
# colors.clear()
# print(colors)

from re import I


a={1,5,6,5,8,4}
b={5,6,8,8,4,4}
c=a.copy()          
u=a.union(b)        #объединение
i=a.intersection(b) #
dl=a.difference(b)  #
dr=b.difference(a)  #

q=a\
    .union(b)\
    .difference(a.intersection(b))