import Data
import recording
# from os import system
# system("cls")
def Buttom_Finish():
    recording.First_name(Data.get_Name())
    recording.Second_name(Data.get_surname())
    recording.Phone_number(Data.get_phone_number())
    recording.Other_information(Data.get_other())

    
def Console_Read():
    path ='Phone_number_folder.csv'
    data=open(path,'r')
    for line in data:
        print(line)
    data.close()

# def Print_Finish():
#     input('Что вы хотите сделать?\n Чтобы записать в книгу нажмите 1.\n Чтобы открыть для прочтения нажмите 2.\n Введите цифру: '))
#     n=input()
#     if n==1:
#         Buttom_Finish()
#     elif n==2:
#         Console_Read()
#     else:
#         print('Вы ввели не корректные данные!')
#         Print_Finish()
        
