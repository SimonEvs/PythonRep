import user_interface

def html_create():
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