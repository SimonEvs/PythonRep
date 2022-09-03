# Напишите программу, которая принимает на вход 5 чисел и находит максимальное из них

# num_1=int(input('Введите первое число: '))
# num_2=int(input('Введите второе число: '))
# num_3=int(input('Введите третье число: '))
# num_4=int(input('Введите четвертое число: '))
# num_5=int(input('Введите пятое число: '))

# if num_1>num_2:
#     a=num_1
# else: a=num_2

# if num_3>num_4:
#     b=num_3
# else: b=num_4
# if a>b:
#     max=a
# else: max=b
# if max>num_5:
#     result=max
# else: result=num_5
# print('Максимальное число')
# print(result)

# Вставлется в конец списка значение в скобках
# my_list=[]
# my_list.append(20)
# my_list.append(20)
# print(my_list)


# range(5)->[0,1,2,3,4]
# range(5, 10)->[5,6,7,8,9]
# range(1, 11, 2)->[1,3,5,7,9]
# my_list=[]
# for i in range(5):
#     num=int(input('--> '))
#     my_list.append(num)
# print(my_list)


# my_list=[3,5,4,9,10]
# print(max(my_list))


# Поиск максимального элемента
# my_list=[3,5,4,9,110]
# maxx=my_list[0]
# for item in my_list[1:]:
#     if item>maxx:
#         maxx=item
# print(maxx)

# Поиск индекса наибольшего элемента
my_list = [3, 5, 4, 9, 110]
maxx_i=0
maxx = my_list[0]
for i in range(1, len(my_list)):
    if my_list[i] > maxx:
        maxx = i
print(maxx, maxx_i)
