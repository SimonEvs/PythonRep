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

# def ResultKN(A,B,C):
#     system("cls") 
#     print(A)
#     print(B)
#     print(C)
#     #if A[0]==B[0]==C[0]==(('X')or('O')) or A[1]==B[1]==C[1]==(('X')or('O')) or A[2]==B[2]==C[2]==(('X')or('O')) or A[0]==A[1]==A[2]==(('X')or('O')) or A[0]==A[1]==A[2]==(('X')or('O')) or B[0]==B[1]==B[2]==(('X')or('O')) or C[0]==C[1]==C[2]==(('X')or('O')) or A[0]==B[1]==C[2]==(('X')or('O')) or A[2]==B[1]==C[0]==(('X')or('O')):
#     if (A[0]==B[0]==C[0]==('X') or A[1]==B[1]==C[1]==('X') 
#         or A[2]==B[2]==C[2]==(('X')) or A[0]==A[1]==A[2]==('X') 
#         or A[0]==A[1]==A[2]==('X') or B[0]==B[1]==B[2]==('X') 
#         or C[0]==C[1]==C[2]==('X') or A[0]==B[1]==C[2]==('X') 
#         or A[2]==B[1]==C[0]==('X')  or   A[0]==B[0]==C[0]==('O') or A[1]==B[1]==C[1]==('O') 
#         or A[2]==B[2]==C[2]==(('O')) or A[0]==A[1]==A[2]==('O') 
#         or A[0]==A[1]==A[2]==('O') or B[0]==B[1]==B[2]==('O') 
#         or C[0]==C[1]==C[2]==('O') or A[0]==B[1]==C[2]==('O') 
#         or A[2]==B[1]==C[0]==('O') ):
        
#         print("Игра окончена")
#         exit()
     

# from os import system

# A = ['-', '-', '-']
# B = ['-', '-', '-']
# C = ['-', '-', '-']

# for i in range(0, 4):
#     first = int(input('Введите место, куда хотете поставить Х '))
#     system("cls")
#     for i in range(0,3):
#         if first==(i+1) and (A[i] != ('O')) and (A[i] != ('X')):
#             A[i]='X'
#             ResultKN(A,B,C)
        
#     for j in range(0,3):
#         if first==(j+4) and (B[j] != ('O')) and (B[j] != ('X')):
#             B[j]='X'
#             ResultKN(A,B,C)
                
#     for k in range(0,3):
#         if first==(k+7) and (C[k] != ('O')) and (C[k] != ('X')):
#             C[k]='X'
#             ResultKN(A,B,C)

#     second = int(input('Введите место, куда хотите поставить О '))
#     system("cls")
#     for i in range(0,3):
#         if second==(i+1) and (A[i] != ('O')) and (A[i] != ('X')):
#             A[i]='O'
#             ResultKN(A,B,C)
    
#     for j in range(0,3):
#         if second==(j+4) and (B[j] != ('O')) and (B[j] != ('X')):
#             B[j]='O'
#             ResultKN(A,B,C)
            
#     for k in range(0,3):
#         if second==(k+7) and (C[k] != ('O')) and (C[k] != ('X')):
#             C[k]='O'
#             ResultKN(A,B,C)


# 4.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# inform=open('Vvod.txt','r')
# n=inform.read()
# inform.close()
# print(n)

# string = n
# count = 1
# data=open('Vivod.txt','w')
# for i in range(len(string)-1):
#     if i <= len(string):
#         if string[i] == string[i + 1]:
#             count += 1
#         else:
#             a = string[i]
#             data.write(f'{count}  {string[i]}\n')
#             count = 1
# data.write(f'{count}  {string[i]}\n')


# Входные и выходные данные хранятся в отдельных текстовых файлах.
