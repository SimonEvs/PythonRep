# 1.Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# text=input("Введите текст: ")
# text_find='абв'
# list1=text.split(' ')
# print(list1)
# list2=[item for item in list1 if text_find not in item]
# print(" ".join(list2))


# 2.Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# def True_or_False_1(n):
#     temp=int(input("Первый вводит число: "))
#     if temp>28:
#         print("Ты ввел не то число! Повтори")
#         # system("cls")
#         return True_or_False_1(n)
#     else:
#         return temp

# def True_or_False_2(n):
#     temp=int(input("Второй вводит число: "))
#     if temp>28:
#         print("Ты ввел не то число! Повтори")
#         # system("cls")
#         return True_or_False_2(n)

#     else:
#         return temp

# from os import system
# system("cls")

# sweets=200
# print('Введите переменную')
# while (sweets!=0):
#     temp_1=True_or_False_1(1)
#     sweets-=temp_1
#     if sweets<=0:
#         print("Первый победил")
#         break
#     print(f"Осталось {sweets} конфет")

#     temp_2=True_or_False_2(1)
#     sweets-=temp_2
#     if sweets<=0:
#         print("второй победил")
#         break
#     print(f"Осталось {sweets} конфет")


# 3.Создайте программу для игры в ""Крестики-нолики"".

def Number_KN(n):
    print('Пример расположения ')
    D = '1 2 3'
    E = '4 5 6'
    F = '7 8 9'
    print(D)
    print(E)
    print(F)
    print()

def Print_ABC(A,B,C):
    print(A)
    print(B)
    print(C)

def First_GO(k):
    first = input('Введите позицию для X ')
    if first !=('O') and first!=('X'):
        if first == 1:
            A[0] = 'X'
        if first == 2:
            A[2] = 'X'
        if first == 3:
            A[4] = 'X'
        if first == 4:
            B[0] = 'X'
        if first == 5:
            B[2] = 'X'
        if first == 6:
            B[4] = 'X'
        if first == 7:
            C[0] = 'X'
        if first == 8:
            C[2] = 'X'
        if first == 9:
            C[4] = 'X'
    else:
        print('Позиция занята!')
        return(k)
    Print_ABC(A,B,C)

def Second_GO(k):
    second = input('Введите позицию для О ')
    if second !=('X') and second !=('O'):
        if second == 1:
            A[0] = input('O')
        if second == 2:
            A[2] = input('O')
        if second == 3:
            A[4] = input('O')
        if second == 4:
            B[0] = input('O')
        if second == 5:
            B[2] = input('O')
        if second == 6:
            B[4] = input('O')
        if second == 7:
            C[0] = input('O')
        if second == 8:
            C[2] = input('O')
        if second == 9:
            C[4] = input('O')
    else:
            print('Позиция занята!')
            return(k)

A = ('- - -')
B = ('- - -')
C = ('- - -')

First_GO(1)
Second_GO(1)
Print_ABC(1)


# 4.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.
