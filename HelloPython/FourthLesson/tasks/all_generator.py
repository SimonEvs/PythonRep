

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


style='style="font-size:22px;"'
    html ='<html>\n  <head></head>\n  <body>\n'
    html +='    <p {}>Name: {} c</p>\n'\
        .format(style,user_interface.First_name_view())
    html +='    <p {}>Surname: {} c</p>\n'\
        .format(style,user_interface.Second_name_view())
    html +='    <p {}>Phone: {} c</p>\n'\
        .format(style,user_interface.Phone_number_view())
    html +='    <p {}>Other: {} c</p>\n'\
        .format(style,user_interface.Other_view())
    html+= '    </body>\n</html>'

    with open('index.html','w') as page:
        page.write(html)
    return html