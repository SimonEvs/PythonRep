import Data
import recording



def First_name_view():
    data=Data.get_Name()
    recording.First_name(data)
    return data

def Second_name_view():
    data=Data.get_surname()
    recording.Second_name(data)
    return data

def Phone_number_view():
    data=Data.get_phone_number()
    recording.Phone_number(data)
    return data

def Other_view():
    data=Data.get_other()
    recording.Other_information(data)
    return data