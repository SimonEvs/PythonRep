# Напишите программу вычисления арифметического выражения заданного строкой.

# new_string = '1 + 2 * 3 + 2'.split()
# for i in range(len(new_string)):
#     if new_string[i].isdigit():
#         new_string[i] = int(new_string[i])
# op_1 = {'+': lambda x, y: x+y, 
# '-': lambda x, y: x-y}
# op_2 = {'*': lambda x, y: x*y, 
# '/': lambda x, y: x/y}

# index = 0
# while ('*' in new_string) or ('/' in new_string):
#     if new_string[index] in op_2:
#         temp = op_2[new_string[index]](new_string[index-1], new_string[index+1])
#         del new_string[index-1:index+2]
#         new_string.insert(index-1, temp)
#         index = 0
#     else:
#         index += 1

# while ('+' in new_string) or ('-' in new_string):
#     if new_string[index] in op_1:
#         temp = op_1[new_string[index]](new_string[index-1], new_string[index+1])
#         del new_string[index-1:index+2]
#         new_string.insert(index-1, temp)
#         index = 0
#     else:
#         index += 1
# print(new_string)

# print(eval('1+2*3+2'))


# Дана последовательность чисел, получить список уникальных элементов.

incomming_list=[1,2,5,7,2,2,1,5,9]
outcoming_list=[i for i in incomming_list if incomming_list.count(i)==1]
print(outcoming_list)

outcoming_list2=list(filter(lambda x: incomming_list.count(x)==1,incomming_list))
print(outcoming_list2)


# Перевод  в Издигит(Издигит - если это цифра)
# a=['1','5','6','7','45','5','+','1','7','6']
# # a=list(map(int,a))
# a=list(map(lambda x:int(x) if x.isdigit() else x,a))
# print(a)