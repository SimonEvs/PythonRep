# Напишите программу, которая будет принимать на вход число и выводить список от -числа, до числа
n = int(input('Vvod '))
for i in range(-n, n+1):
    print(f'*{i}*')


# Напишите программу, которая будет принимать на
# вход дробь и показывать первую цифру дробной части числа
number = float(input("Ввод"))
number *= 10
print(number)
number = int(number)
print(number)
print(number % 10)


# Напишите программу, которая будет принимать на вход число и проверть кратно
# оно (5 и 10) или (15, но не 30)

num = int(input("Введите число "))
if ((num % 5 == 0) and (num % 10 == 0) or ((num % 15 == 0) and (num % 30 != 0))):
    print("Yes")
else: print("No")