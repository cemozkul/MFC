from inputs import *

def welcome():
    print('Hi welcome to MFC ! \nPlease Write Selecet Your User Type \nPlease Make Sure Your Responses Are "CAPITAL"! \nLogin with "L" \nRegister with "R" \nExit with "X" \nAnytime You Want to Exit You Can Press "X" \n!!! HAVE FUN !!!')
welcome()

while True:
    first_input = type()
    if first_input == 'L':
        username, password = login()
    elif first_input == 'R':
        username, password = register_pt_1()
    elif first_input == 'X':
        break
    else:
        print('Please Enter Valid command !')