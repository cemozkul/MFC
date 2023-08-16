def type():
    first_input = input('Please Write Your Command: ')
    return first_input

def login():
    username = input('Username: ')
    password = input('Password: ')
    return username, password

def register_pt_1():
    print("Please Select Unique Username and Password. \nPlease Make Sure Your password Does'nt Contain Your Username ")
    username = input('Username: ')
    password = input('Password: ')
    return username, password

def register_pt_2():
    return