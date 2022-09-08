# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 0, 56 -> 11

# a = str(input('Введите вещественное число '))
# sum = 0
# for i in range(0, len(a)):
#     if a[i] == (",") or a[i]==("."):
#         continue
#     sum += int(a[i])
# print(f'Сумма цифр = {sum}')


# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда[1, 2, 6, 24](1, 1*2, 1*2*3, 1*2*3*4)

# my_list=[]
# N=int(input("Введите число "))
# i=0
# temp=1
# while i<N:
#     temp*=(i+1)
#     my_list.append(temp)
#     i+=1
# print(my_list)


# Задайте список из k чисел последовательности(1 + 1\k) ^ k и выведите на экран их сумму.

# my_list=[]
# N=int(input("Введите число "))
# i=0
# temp=1
# while i<N:
#     temp=((1+1/(i+1))**(i+1))
#     my_list.append(round(temp,3))
#     i+=1
# print(my_list)


# Задайте список из N элементов, заполненных числами из промежутка[-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.


# from random import randint, random


# my_numbers = []
# my_index = []
# N = int(input("Введите число "))
# i = 0
# temp = 1
# while i < N:
#     temp = randint(-N, N)
#     my_numbers.append(temp)
#     i += 1
# print(my_numbers)
# nums = str(input("Введите индексы через пробел "))
# print(len(nums))
# i = 0
# for i in range(0, len(nums)):
#     if nums[i] == range(-N, N):
#         if nums[i] == (" "):

#             continue
#     my_index.append(nums[i])
# print(my_index)

# Реализуйте алгоритм перемешивания списка.

from random import randint


mass = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'Изначальный массив {mass}')
n = 8
i=0
while i < 8:
    random_index=randint(0,n-i)
    temp =mass[random_index]
    mass[random_index]=mass[i]
    mass[i] = temp
    i+=1
print(f'Перемешанный массив {mass}')