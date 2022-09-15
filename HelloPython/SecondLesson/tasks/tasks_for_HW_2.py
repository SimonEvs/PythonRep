# 1.Вычислить число c заданной точностью d

# def Find_Number(k):
#     import math
#     n = math.pi
#     print(f'Ответ: {round(n,k)}')


# print('Введите число, до какого знака после запятой хотите округлить:')
# find = input()
# Find_Number(int(find))


# 2.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

# def Manuscript(number):
#     my_list = []
#     for i in range(1, number+1):
#         if (number % i == 0):
#             my_list.append(i)
#     print(my_list)


# Manuscript(20)


# 3.Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

# def Find_once(new_list):
#     final_list=[]
#     for i in new_list:
#         if new_list.count(i)==1:
#             final_list.append(i)
#     print(final_list)

# my_list = [1, 1, 2, 3, 4, 4, 5, 5,8]
# Find_once(my_list)


# 4.Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# import random

# my_list=[]
# for i in range(0,3):
#     my_list.append(random.randint(0,100))

# print(my_list)
# print('Остальное в текстовом файле answer.txt')
# if my_list[0]>0 and my_list[1]>0 and my_list[2]>0:
#     with open(r'HelloPython\SecondLesson\tasks\answer.txt','w') as data:
#         data.write(f'{my_list[0]}x^2 + {my_list[1]}x + {my_list[2]} = 0')

# elif my_list[0]>0 and my_list[1]>0 and my_list[2]<0:
#      with open(r'HelloPython\SecondLesson\tasks\answer.txt','w') as data:
#         data.write(f'{my_list[0]}x^2 + {my_list[1]}x = 0')

# elif my_list[0]>0 and my_list[1]<0 and my_list[2]>0:
#      with open(r'HelloPython\SecondLesson\tasks\answer.txt','w') as data:
#          data.write(f'{my_list[0]}x^2 + {my_list[2]} = 0')

# elif my_list[0]<0 and my_list[1]>0 and my_list[2]>0:
#     with open(r'HelloPython\SecondLesson\tasks\answer.txt','w') as data:
#         data.write(f'{my_list[1]}x + {my_list[2]} = 0')

# elif my_list[0]>0 and my_list[1]<0 and my_list[2]<0:
#      with open(r'HelloPython\SecondLesson\tasks\answer.txt','w') as data:
#         data.write(f'{my_list[0]}x^2 = 0')

# elif my_list[0]<0 and my_list[1]>0 and my_list[2]<0:
#      with open(r'HelloPython\SecondLesson\tasks\answer.txt','w') as data:
#         data.write(f'{my_list[1]}x = 0')

# elif my_list[0]<0 and my_list[1]<0 and my_list[2]>0:
#      with open(r'HelloPython\SecondLesson\tasks\answer.txt','w') as data:
#         data.write(f'{my_list[2]} = 0')
# else:
#      with open(r'HelloPython\SecondLesson\tasks\answer.txt','w') as data:
#         data.write(f'0 = 0')


# 5.Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
path = 'Python\HelloPython\SecondLesson\tasks\first.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

exit()