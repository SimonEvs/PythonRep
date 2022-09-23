import Data
import recording

def Buttom_Finish():
    recording.First_name(Data.get_Name())
    recording.Second_name(Data.get_surname())
    recording.Phone_number(Data.get_phone_number())
    recording.Other_information(Data.get_other())

# Finish()