
# В файле находится N натуральных чисе, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i]-1=A[i-1].
# Найдите это число

# f1 = open('1Task.txt', 'r')
# output1 = f1.read()
# nlist = output1.split(' ')
# print(nlist)

# Первое решение
# for i in range(1, len(nlist)):
#     if int(nlist[i])-1 != int(nlist[i-1]):
#         numb = int(nlist[i])-1
# print(numb)

# Второе решение
# my_list=[int(nlist[i])-1 for i in range(1,len(nlist)) if int(nlist[i])-1 != int(nlist[i-1])]
# print(my_list)


# Дан список чисел. Создайте список, в который попадают числа,
# описывающие возратающую последовательность. Порядок элементов менять нельзя.

# my_list = [7, 5, 3, 9, 2, 3, 5, 11, 8, 5]
# count=0
# new_list = [my_list[i] for i in range(1,len(my_list))  if (my_list[i] >= max(my_list[0:i]))]
# new_list.insert(0,my_list[0])
# print(new_list)

# Напишите программу, которая удаляет из текста слова, содержащие "абв".


text='Мы неабв очень любим Питон иабв Джавабв'

text_find='абв'
list1=text.split(' ')
print(list1)
list2=[item for item in list1 if text_find not in item]
print(list2)


