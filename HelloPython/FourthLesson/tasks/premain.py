from os import system
import modelist
import all_generator
system("cls")
def Oblozka():
    n=input('Что вы хотите сделать?\n Чтобы записать в книгу нажмите 1.\n \
    Чтобы открыть для прочтения нажмите 2.\n Введите цифру: ')
        
    if n=='1':
        all_generator.Finish_prog()
    elif n=='2':
        modelist.Console_Read()
    else:
        system("cls")
        print('Вы ввели не корректные данные!')
        Oblozka()