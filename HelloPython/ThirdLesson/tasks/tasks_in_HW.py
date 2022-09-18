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

def True_or_False_1(n):
    temp=int(input("Первый вводит число: "))
    if temp>28:
        print("Ты ввел не то число! Повтори")
        # system("cls")
        return True_or_False_1(n)
    else: 
        return temp
        
def True_or_False_2(n):
    temp=int(input("Второй вводит число: "))
    if temp>28:
        print("Ты ввел не то число! Повтори")
        # system("cls")
        return True_or_False_2(n)
        
    else: 
        return temp

from os import system
system("cls")

sweets=200
print('Введите переменную')
while (sweets!=0):
    temp_1=True_or_False_1(1)
    sweets-=temp_1
    if sweets<=0:
        print("Первый победил")
        break
    print(f"Осталось {sweets} конфет")

    temp_2=True_or_False_2(1)
    sweets-=temp_2
    if sweets<=0:
        print("второй победил")
        break
    print(f"Осталось {sweets} конфет")


        
   
    
    
    # if temp1>28:
    #     temp1=input('Ты играешь не по правилам, введи число до 28!!! Число: ') 
    #     if temp1>28:
    #     temp1=input('Ты играешь не по правилам, введи число до 28!!! Число: ')
    # temp2=int(input("Второй ходит: "))
    # if temp2>28:
    #     temp2=input('Ты играешь не по правилам, введи число до 28!!! Число: ')
    # sweets-=temp1
    # player_1+=temp1
    # print(f'Количество конфет первого {player_1}')
    # sweets-=temp2
    # player_2+=temp2
    # print(f'Количество конфет второго {player_2}')
    # temp1,temp2=0,0
    # print(f"Осталось {sweets} конфет")
    


# 3.Создайте программу для игры в ""Крестики-нолики"".

# 4.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.