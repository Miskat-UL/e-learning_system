import json


st_login_file = 'student_login_data.json'
def login_data():
    print("Now create an account....")
    email = input("enter your email: ")
    password = input("Enter password: ")
    extra_key = input("enter something you like the most(in case of password reset): ")

    context = {
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
    pass