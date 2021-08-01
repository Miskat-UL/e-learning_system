import json
from utils import teacher_info
file_name = 'teacher_json_data.json'


def account_create_data():
    name = input("enter your name: ")
    age = input("enter your age: ")
    speciality = input("Enter the subjects you want to teach(separeted with commas): ").split(",")
    address = input('enter your address:')
    teacher_info.login_data(name)

    context = {
        'name': name,
        'age': age,
        'class_name': speciality,
        'address': address
    }

    with open(file_name, 'r+') as file:
        data = json.load(file)
        data.append(context)
        file.seek(0)
        json.dump(data, file, indent=2)



