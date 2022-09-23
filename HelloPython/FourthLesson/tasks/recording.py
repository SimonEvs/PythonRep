import Data 


def First_name(name):
    with open('Phone_number_folder.csv', 'a') as file:
        file.write('Name: {}\n'
                   .format(name))


def Second_name(surname):
    with open('Phone_number_folder.csv', 'a') as file:
        file.write('Surname: {}\n'
                   .format(surname))


def Phone_number(phone):
    with open('Phone_number_folder.csv', 'a') as file:
        file.write('Phone number: {}\n'
                   .format(phone))


def Other_information(other):
    with open('Phone_number_folder.csv', 'a') as file:
        file.write('Other: {}\n'
                   .format(other))


# First_name(Data.get_Name())
# Second_name(Data.get_surname())
# Phone_number(Data.get_phone_number())
# Other_information(Data.get_other())