from os import system
system("cls")
import modelist

# modelist.Print_Finish()
n=input('Что вы хотите сделать?\n Чтобы записать в книгу нажмите 1.\n \
Чтобы открыть для прочтения нажмите 2.\n Введите цифру: ')
    
if n=='1':
    modelist.Buttom_Finish()
elif n=='2':
    modelist.Console_Read()
else:
    print('Вы ввели не корректные данные!')