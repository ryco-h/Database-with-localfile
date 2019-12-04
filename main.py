import re
import sys
from os import system
import os


def registration():
    system('cls')
    file = open(folder + r'\\contain.py')
    read = file.read()

    data = input("User :")
    data2 = input("Password :")
    user1 = (data, data2)
    
    # Uses a RE to find bracket, so it will change the close bracket as a new data from input
    # And it also contains a new close bracket
    search = re.sub("]", str(user1), read)
    
    # Finds the close parenthesis and changes it to comma 
    # data = [(example1, example2)]
    # and it will change like this
    # data = [(example1, example2), (example3, example4)]
    tuples = re.findall("[)]", read)
    if tuples:
        search = re.sub("]", (', ' + str(user1)), read)
        
    # Overwrites the data to the contain file
    file2 = open(folder + r'\\contain.py', "w")
    file2.write(search + "]")
    print("Register successful.\n\n")


def login():

    system('cls')
    user = input("Username : ")
    password = input("Password : ")

    if (user, password) in con.data:
        print("Logged in.\n")
    else:
        print("Failed.\n")


if __name__ == '__main__':
  
    # Location of your file
    folder = os.path.dirname(__file__)
    
    try:
        import contain as con
    except ModuleNotFoundError:
        with open(folder + r"\\contain.py", "w") as files:
        # Writes a list to avoid an error
            files.write("data = []")

    while True:
        choice = input("[1] Login\n[2] Registration\n[3] Exit\n\nYour choice : ")
        if choice == '1':
            login()
        elif choice == '2':
            registration()
        elif choice == '3':
            sys.exit()
        else:
            print('Wrong input!')
