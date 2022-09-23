
# path = 'Phone_numbersfolder.txt'
data=567

def First_name(data):
    with open('Phone_number_folder.csv','a') as file:
        file.write('Name;{}\n'
                        .format(data))


def Second_name(data):
    with open('Phone_number_folder.csv','a') as file:
        file.write('Surname;{}\n'
                        .format(data))


def Phone_number(data):
    with open('Phone_number_folder.csv','a') as file:
        file.write('Phone number;{}\n'
                        .format(data))

def Other_information(data):
    with open('Phone_number_folder.csv','a') as file:
        file.write('Other;{}\n'
                        .format(data))

First_name(data)
Second_name(data)