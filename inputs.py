import csv

def type():
    first_input = input('Please Write Your Command: ')
    return first_input

def login():
    username = input('Username: ')
    password = input('Password: ')
    
    if login_checker(username, password, 'user.csv'):
        print("Login successful!")
    else:
        print("Login failed. Invalid username or password.")
        
    return username, password

def login_checker(username, password, filename):
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['username'] == username and row['password'] == password:
                return True
            
    return False
def register_pt_1():
    print("Please Select Unique Username and Password. \nPlease Make Sure Your password Does'nt Contain Your Username ")
    username = input('Username: ')
    password = input('Password: ')
    return username, password

def register_pt_2():
    
    return