
#a-открытие для добавления данных; r- для чтения; w-  для записи

# with open('file.txt','w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')




# colors=['red','greennnnn','blue']
# data=open('file.txt','w') 
# data.writelines(colors) #Разделений не будет
# data.write('\nLine 2\n')
# data.write('Line 3\n')
# data.close()



# exit() #exit()- отменяет код, который записан ниже
path ='file.txt'
data=open(path,'r')
for line in data:
    print(line)
data.close()