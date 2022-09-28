import Data
def Finish_prog():
    first=Data.get_Name()
    second=Data.get_surname()
    phone=Data.get_phone_number()
    other=Data.get_other()
    xml= '<xml>\n'
    xml+= ' <Name units ="c">{}</name>\n'\
        .format(first)
    xml+= ' <Second units ="c">{}</surname>\n'\
        .format(second)
    xml+= ' <Phone Number units ="c">{}</phone>\n'\
        .format(phone)
    xml+= ' <Other units ="c">{}</other>\n'\
        .format(other)

    with open('phonebook.xml','w') as page:
        page.write(xml)



    with open('Phone_number_folder.csv', 'a') as file:
        file.write('Name: {}\n'
            .format(first))

    with open('Phone_number_folder.csv', 'a') as file:
        file.write('Surname: {}\n'
            .format(second))

    with open('Phone_number_folder.csv', 'a') as file:
        file.write('Phone number: {}\n'
            .format(phone))

    with open('Phone_number_folder.csv', 'a') as file:
        file.write('Other: {}\n'
            .format(other))


    style='style="font-size:22px;"'
    html ='<html>\n  <head></head>\n  <body>\n'
    html +='    <p {}>Name: {} c</p>\n'\
        .format(style,first)
    html +='    <p {}>Surname: {} c</p>\n'\
        .format(style,second)
    html +='    <p {}>Phone: {} c</p>\n'\
        .format(style,phone)
    html +='    <p {}>Other: {} c</p>\n'\
        .format(style,other)
    html+= '    </body>\n</html>'

    with open('phonebook.html','w') as page:
        page.write(html)