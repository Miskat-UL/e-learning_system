import json
from utils import teacher_login_info

te_information_file = 'teacher_json_data.json'


def account_create_data():
    name = input("enter your name: ")
    age = input("enter your age: ")
    speciality = input("Enter the subjects you want to teach(separeted with commas): ").split(",")
    address = input('enter your address:')
    teacher_login_info.login_data(name)

    context = {
        'name': name,
        'age': age,
        'class_name': speciality,
        'address': address
    }

    with open(te_information_file, 'r+') as file:
        data = json.load(file)
        data.append(context)
        file.seek(0)
        json.dump(data, file, indent=2)



