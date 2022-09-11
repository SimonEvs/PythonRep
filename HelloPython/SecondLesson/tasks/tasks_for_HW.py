# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# my_list= [2, 3, 5, 9, 3]
# sum=0
# for i in range(0, len(my_list)):
#     if (i % 2)>0:
#         sum+=my_list[i]
# print(f'Сумма нечетных равна = {sum}')


# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

# my_list = [5, 6, 7, 8, 9,3, 4, 65, 55]
# new_list = []
# for index in range(0, 9):
#     sum = my_list[index]*my_list[len(my_list)-1-index]
#     if (my_list[index]==my_list[len(my_list)-1-index]) or(my_list[index+1]==my_list[len(my_list)-1-index]):
#         new_list.append(sum)
#         break
#     new_list.append(sum)
#     sum=0
# print(new_list)


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.

# from lib2to3.pgen2.token import INDENT
# from unittest import result


# my_list = [10005.5, 6.1, 7.3, 8.05, 9.01, 3.09, 4.0055, 65.0033, 55.2]
# new_list = []
# for i in range(0, len(my_list)):
#     temp = (((my_list[i] % 10)*10) % 10/10)
#     # result=round(temp,10)
#     new_list.append(temp)
# print(new_list)
# x=max(new_list)-min(new_list)
# x=round(x,3)
# print(f'Разница = {x}')



# Напишите программу, которая будет преобразовывать десятичное число в двоичное(без встроенных функций).

# Пример:
# def Ten_to_two(x)

# if n>2:


#     return Ten_to_two(n)

result = []
def Ten_to_two(x):
    if (x == 0):
        return l
    temp = x % 2
    result.append(temp)
    Ten_to_two(x // 2)
a = int(input("Введите число: "))
Ten_to_two(a)
result.reverse()
print("Двоичная форма числа:")
for i in l:
    print(i,end='')

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21, 13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
