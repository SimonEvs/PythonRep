from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import pressure_view


def create(device=1):
    xml= '<xml>\n'
    xml+= ' <temperature units ="c">{}</temperature>\n'\
        .format(temperature_view(device))
    xml+= ' <wind_speed units ="c">{}</wind_speed>\n'\
        .format(wind_speed_view(device))
    xml+= ' <pressure units ="c">{}</pressure>\n'\
        .format(pressure_view(device))

    with open('data.xml','w') as page:
        page.write(xml)
    return xml