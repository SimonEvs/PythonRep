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

# def Number_KN(n):
#     print('Пример расположения ')
#     D = '1 2 3'
#     E = '4 5 6'
#     F = '7 8 9'
#     print(D)
#     print(E)
#     print(F)
#     print()

# def Print_ABC(A,B,C):
#     print(A)
#     print(B)
#     print(C)
from os import system

A = ['-', '-', '-']
B = ['-', '-', '-']
C = ['-', '-', '-']

for i in range(0, 4):
    # def First_GO(A,B,C):
    first = int(input('Введите переменную '))
    system("cls")
# if A[ !=('O') and first!=('X'):
    if (first == 1) and (A[0] != ('O')) and (A[0] != ('X')):
        A[0] = 'X'
    if first == 2 and A[1] != ('O') and A[1] != ('X'):
        A[1] = 'X'
    if first == 3 and A[2] != ('O') and A[2] != ('X'):
        A[2] = 'X'
    if first == 4 and B[0] != ('O') and B[0] != ('X'):
        B[0] = 'X'
    if first == 5 and B[1] != ('O') and B[1] != ('X'):
        B[1] = 'X'
    if first == 6 and B[2] != ('O') and B[2] != ('X'):
        B[2] = 'X'
    if first == 7 and C[0] != ('O') and C[0] != ('X'):
        C[0] = 'X'
    if first == 8 and C[1] != ('O') and C[1] != ('X'):
        C[1] = 'X'
    if first == 9 and C[2] != ('O') and C[2] != ('X'):
        C[2] = 'X'
    print(A)
    print(B)
    print(C)
    
# else:
#     print('Позиция занята!')
    # return(First_GO(A,B,C))
# Print_ABC(A,B,C)

# def Second_GO(A,B,C):
    second = int(input('Введите переменную '))
    system("cls")
# if second !=('X') and second !=('O'):
    if second == 1 and (A[0] != ('O')) and (A[0] != ('X')):
        A[0] = 'O'
    if second == 2 and A[1] != ('O') and A[1] != ('X'):
        A[1] = 'O'
    if second == 3 and A[2] != ('O') and A[2] != ('X'):
        A[2] = 'O'
    if second == 4 and B[0] != ('O') and B[0] != ('X'):
        B[0] = 'O'
    if second == 5 and B[1] != ('O') and B[1] != ('X'):
        B[1] = 'O'
    if second == 6 and B[2] != ('O') and B[2] != ('X'):
        B[2] = 'O'
    if second == 7 and C[0] != ('O') and C[0] != ('X'):
        C[0] = 'O'
    if second == 8 and C[1] != ('O') and C[1] != ('X'):
        C[1] = 'O'
    if second == 9 and C[2] != ('O') and C[2] != ('X'):
        C[2] = 'O'
    print(A)
    print(B)
    print(C)

    if (A[0]==B[0]==C[0]) or (A[1]==B[1]==C[1] or (A[2]==B[2]==C[2]) or (A[0]==A[1]==A[2]) or (A[0]==A[1]==A[2]) or (B[0]==B[1]==B[2]) or (C[0]==C[1]==C[2]) or (A[0]==B[1]==C[2]) or (A[2]==B[1]==C[0])):
        print("Игра окончена")
# else:
#         print('Позиция занята!')
#         # return(Second_GO(A,B,C))


# for i in range(0,9):
#     First_GO(A,B,C)
#     Second_GO(A,B,C)
#     Print_ABC(A,B,C)


# 4.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.
