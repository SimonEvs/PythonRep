import user_interface
def create1():
    xml= '<xml>\n'
    xml+= ' <Name units ="c">{}</name>\n'\
        .format(user_interface.First_name_view())
    xml+= ' <Second units ="c">{}</surname>\n'\
        .format(user_interface.Second_name_view())
    xml+= ' <Phone Number units ="c">{}</phone>\n'\
        .format(user_interface.Phone_number_view())
    xml+= ' <Other units ="c">{}</other>\n'\
        .format(user_interface.Other_view())

    with open('phonebook.xml','w') as page:
        page.write(xml)
    return xml