# 2.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

# def Manuscript(number):
#     my_list = []
#     for i in range(1, number+1):
#         if (number % i == 0):
#             my_list.append(i)
#     print(my_list)

# def Manuscript(number):
#     my_list = [i for i in range(1,number+1) if (number%i==0)]
#     print(my_list)


# Manuscript(20)



#3.Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

# def Find_once(new_list):
#     final_list=[]
#     for i in new_list:
#         if new_list.count(i)==1:
#             final_list.append(i)
#     print(final_list)



# def Find_once(new_list):
#     final_list=[i for i in new_list if new_list.count(i)==1]     
#     print(final_list)

# my_list = [1, 1, 2, 3, 4, 4, 5, 5,8]
# Find_once(my_list)





