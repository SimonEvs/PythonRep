



new_string = '1 + 2 * 3 + 2'.split()
for i in range(len(new_string)):
    if new_string[i].isdigit():
        new_string[i] = int(new_string[i])
op_1 = {'+': lambda x, y: x+y, 
'-': lambda x, y: x-y}
op_2 = {'*': lambda x, y: x*y, 
'/': lambda x, y: x/y}

index = 0
while '*' in new_string or '/' in new_string:
    if new_string[index] in op_2:
        temp = op_2[new_string[index]](new_string[index-1], new_string[index+1])
        del new_string[index-1:index+2]
        new_string.insert(index-1, temp)
        index = 0
    else:
        index += 1

while '+' in new_string or '-' in new_string:
    if new_string[index] in op_1:
        temp = op_1[new_string[index]](new_string[index-1], new_string[index+1])
        del new_string[index-1:index+2]
        new_string.insert(index-1, temp)
        index = 0
    else:
        index += 1
print(new_string)

print(eval('1+2*3+2'))
