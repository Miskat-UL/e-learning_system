import json
import random

from file_outputs import Files

te_login_file = 'teacher_login_data.json'

_file = Files(te_login_file)

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
        'username': name,
        'email': email,
        'password': password,
        'extra_key': extra_key,

    }
    with open(te_login_file, 'r+') as file:
        data = json.load(file)
        data.append(context)
        file.seek(0)
        json.dump(data, file, indent=2)

    print(f"Your username is: {username}")
    print(f"Your password is: {password}")
    print("do not forget your username and password")


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")





