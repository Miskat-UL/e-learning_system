import json
import random

from file_outputs import Files
st_login_file = 'student_login_data.json'
_file = Files(st_login_file)


def login_data(name):
    print("Now create an account....")
    email = input("enter your email: ")
    password = input("Enter password: ")
    extra_key = input("enter something you like the most(in case of password reset): ")
    for _ in range(random.randint(2, 4)):
        digits = str(random.randint(0, 9))
        name += digits
    username = name
    context = {
        'username': username,
        'email': email,
        'password': password,
        'extra_key': extra_key
    }
    with open(st_login_file, 'r+') as file:
        data = json.load(file)
        data.append(context)
        file.seek(0)
        json.dump(data, file, indent=2)


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    file_content = _file.file_output()

    for value in file_content:
        prev_entry = False
        while not prev_entry:
            if value["username"] == username:
                prev_entry = True
                entry = False
                while not entry:
                    if value['password'] == password:
                        entry = True
                        print("success entry. Going to your profile!! ")
                        login_after_menu()
                    else:
                        password = input("wrong password. Enter your password again: ")
            else:
                username = input("wrong username. Enter your username again: ")

def login_after_menu():
    pass