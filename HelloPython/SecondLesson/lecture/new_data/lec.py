
#a-открытие для добавления данных; r- для чтения; w-  для записи.

# with open('file2.txt','w') as data:
#     data.write('line 1111\n')
#     data.write('line 2\n')




# colors=['red','greennnnn','blue']
# data=open('file.txt','w') 
# data.writelines(colors) #Разделений не будет
# data.write('\nLine 2\n')
# data.write('Line 3\n')
# data.close()



# exit() #exit()- отменяет код, который записан ниже
# path ='file.txt'
# data=open(path,'r')
# for line in data:
#     print(line)
# data.close()





# import example
# print(example.f(1))

# Или можно использовать 

# import example as ex
# print(ex.f(1))



path ='file.txt'
f=open(path,'r')
data=f.read()+' '
f.close()